"""
GameplayScene - Main game scene for playing Tetris
"""

import pygame
from src.constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, BOARD_OFFSET_X, BOARD_OFFSET_Y,
    CELL_SIZE, BOARD_WIDTH, BOARD_HEIGHT, COLOR_BACKGROUND,
    COLOR_BOARD_BG, COLOR_GRID_LINE, COLOR_TEXT, COLOR_TEXT_HUD,
    INITIAL_DROP_INTERVAL, MIN_DROP_INTERVAL, LEVEL_SPEED_DECREASE,
    FONT_NAME, FONT_SIZE_LARGE, FONT_SIZE_MEDIUM, FONT_SIZE_SMALL,
    TEXT_NEXT, TEXT_SCORE, TEXT_LEVEL, TEXT_LINES,
    TEXT_GAME_OVER, TEXT_FINAL_SCORE, TEXT_RESTART_HINT, TEXT_OPERATION_HINT
)
from src.models.board import Board
from src.models.tetromino_factory import TetrominoFactory


class GameplayScene:
    # Key repeat settings
    KEY_REPEAT_INITIAL = 150    # ms before first repeat
    KEY_REPEAT_INTERVAL = 50    # ms between repeats

    def __init__(self, app):
        self.app = app
        self.board = Board()
        self.factory = TetrominoFactory()
        self.current_tetromino = None
        self.next_tetromino = None
        self.game_over = False
        self.last_drop_time = 0
        self.drop_interval = INITIAL_DROP_INTERVAL

        # Key repeat tracking
        self.keys_held = {}
        self.keys_repeat_timers = {}

        # Preload font
        self.font_large = pygame.font.SysFont(FONT_NAME, FONT_SIZE_LARGE)
        self.font_medium = pygame.font.SysFont(FONT_NAME, FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.SysFont(FONT_NAME, FONT_SIZE_SMALL)

        self._spawn_tetromino()

    def _spawn_tetromino(self):
        """Spawn the next tetromino or get a new one"""
        if self.next_tetromino is None:
            self.next_tetromino = self.factory.get_random_tetromino()

        self.current_tetromino = self.next_tetromino
        spawn_x, spawn_y = self.current_tetromino.get_spawn_position(BOARD_WIDTH)
        self.current_tetromino.set_position(spawn_x, spawn_y)

        self.next_tetromino = self.factory.get_random_tetromino()

        # Check if game over
        if not self.board.can_spawn(self.current_tetromino):
            self.game_over = True

    def _handle_event(self, event):
        """Handle pygame events"""
        if event.type == pygame.KEYDOWN:
            if self.game_over:
                if event.key in (pygame.K_r,):
                    self._restart_game()
                elif event.key == pygame.K_ESCAPE:
                    self.app.change_scene("menu")
            else:
                self._handle_input(event)
                # Start key repeat tracking
                self._start_key_repeat(event.key)

        elif event.type == pygame.KEYUP:
            # Stop key repeat tracking
            self._stop_key_repeat(event.key)

    def _start_key_repeat(self, key):
        """Start tracking a key for repeat"""
        self.keys_held[key] = True
        self.keys_repeat_timers[key] = 0

    def _stop_key_repeat(self, key):
        """Stop tracking a key"""
        self.keys_held.pop(key, None)
        self.keys_repeat_timers.pop(key, None)

    def _handle_input(self, event):
        """Handle single key press input"""
        key = event.key

        # Direction mapping
        if key in (pygame.K_LEFT, pygame.K_a):
            self._move_tetromino(-1, 0)
        elif key in (pygame.K_RIGHT, pygame.K_d):
            self._move_tetromino(1, 0)
        elif key in (pygame.K_DOWN, pygame.K_s):
            self._move_down()
        elif key in (pygame.K_UP, pygame.K_w):
            self._rotate_tetromino()
        elif key == pygame.K_SPACE:
            self._hard_drop()

    def _process_key_repeat(self, current_time):
        """Process held keys for repeat actions"""
        if self.game_over:
            return

        keys_to_update = []

        for key, timer in self.keys_repeat_timers.items():
            elapsed = current_time - timer
            if elapsed >= self.KEY_REPEAT_INTERVAL:
                keys_to_update.append((key, current_time))

        for key, timestamp in keys_to_update:
            self.keys_repeat_timers[key] = timestamp
            # Execute repeat action
            if key in (pygame.K_LEFT, pygame.K_a):
                self._move_tetromino(-1, 0)
            elif key in (pygame.K_RIGHT, pygame.K_d):
                self._move_tetromino(1, 0)
            elif key in (pygame.K_DOWN, pygame.K_s):
                self._move_down()

    def _move_tetromino(self, dx, dy):
        """Try to move tetromino, don't move if collision"""
        test_tetromino = self.current_tetromino.copy()
        test_tetromino.move(dx, dy)

        if not self.board.is_collision(test_tetromino):
            self.current_tetromino.move(dx, dy)
            return True
        return False

    def _rotate_tetromino(self):
        """Try to rotate tetromino, revert if collision"""
        test_tetromino = self.current_tetromino.copy()
        test_tetromino.rotate()

        # Wall kick - try shifting left/right if rotation fails
        if self.board.is_collision(test_tetromino):
            test_tetromino.move(-1, 0)
            if self.board.is_collision(test_tetromino):
                test_tetromino.move(2, 0)
                if self.board.is_collision(test_tetromino):
                    return  # Cannot rotate

        self.current_tetromino.blocks = test_tetromino.blocks
        self.current_tetromino.rotation_state = test_tetromino.rotation_state

    def _move_down(self):
        """Move tetromino down one row"""
        if not self._move_tetromino(0, 1):
            self._lock_tetromino()

    def _hard_drop(self):
        """Drop tetromino to the bottom instantly"""
        while self._move_tetromino(0, 1):
            pass
        self._lock_tetromino()

    def _lock_tetromino(self):
        """Lock current tetromino and spawn next"""
        self.board.lock_tetromino(self.current_tetromino)
        self.board.clear_lines()
        self._spawn_tetromino()

    def _restart_game(self):
        """Restart the game"""
        self.board.reset()
        self.factory = TetrominoFactory()
        self.current_tetromino = None
        self.next_tetromino = None
        self.game_over = False
        self.drop_interval = INITIAL_DROP_INTERVAL
        self._spawn_tetromino()

    def update(self, current_time):
        """Update game state based on time"""
        if self.game_over:
            return

        # Process key repeat for held keys
        self._process_key_repeat(current_time)

        self.drop_interval = self.board.get_drop_interval(
            INITIAL_DROP_INTERVAL, MIN_DROP_INTERVAL, LEVEL_SPEED_DECREASE
        )

        if current_time - self.last_drop_time > self.drop_interval:
            self._move_down()
            self.last_drop_time = current_time

    def render(self, screen):
        """Render the game"""
        screen.fill(COLOR_BACKGROUND)

        # Draw board background
        board_rect = pygame.Rect(
            BOARD_OFFSET_X, BOARD_OFFSET_Y,
            BOARD_WIDTH * CELL_SIZE, BOARD_HEIGHT * CELL_SIZE
        )
        pygame.draw.rect(screen, COLOR_BOARD_BG, board_rect)

        # Draw grid lines
        for x in range(BOARD_WIDTH + 1):
            pygame.draw.line(
                screen, COLOR_GRID_LINE,
                (BOARD_OFFSET_X + x * CELL_SIZE, BOARD_OFFSET_Y),
                (BOARD_OFFSET_X + x * CELL_SIZE, BOARD_OFFSET_Y + BOARD_HEIGHT * CELL_SIZE)
            )
        for y in range(BOARD_HEIGHT + 1):
            pygame.draw.line(
                screen, COLOR_GRID_LINE,
                (BOARD_OFFSET_X, BOARD_OFFSET_Y + y * CELL_SIZE),
                (BOARD_OFFSET_X + BOARD_WIDTH * CELL_SIZE, BOARD_OFFSET_Y + y * CELL_SIZE)
            )

        # Draw locked blocks
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.board.grid[y][x] is not None:
                    self._draw_block(
                        screen, x, y, self.board.grid[y][x]
                    )

        # Draw current tetromino
        if self.current_tetromino and not self.game_over:
            for bx, by in self.current_tetromino.get_blocks():
                if by >= 0:  # Only draw if on screen
                    self._draw_block(
                        screen, bx, by, self.current_tetromino.color
                    )

        # Draw next tetromino preview
        self._draw_next_preview(screen)

        # Draw HUD
        self._draw_hud(screen)

        # Draw operation hint
        self._draw_operation_hint(screen)

        # Draw game over overlay
        if self.game_over:
            self._draw_game_over(screen)

    def _draw_block(self, screen, x, y, color):
        """Draw a single block at grid position"""
        rect = pygame.Rect(
            BOARD_OFFSET_X + x * CELL_SIZE + 1,
            BOARD_OFFSET_Y + y * CELL_SIZE + 1,
            CELL_SIZE - 2, CELL_SIZE - 2
        )
        pygame.draw.rect(screen, color, rect)

    def _draw_next_preview(self, screen):
        """Draw next tetromino preview"""
        preview_x = BOARD_OFFSET_X + BOARD_WIDTH * CELL_SIZE + 30
        preview_y = BOARD_OFFSET_Y + 50

        # Label
        label = self.font_medium.render(TEXT_NEXT, True, COLOR_TEXT)
        screen.blit(label, (preview_x, preview_y - 30))

        # Draw next tetromino
        if self.next_tetromino:
            for bx, by in self.next_tetromino.blocks:
                block_x = preview_x + bx * CELL_SIZE
                block_y = preview_y + by * CELL_SIZE
                rect = pygame.Rect(block_x, block_y, CELL_SIZE - 2, CELL_SIZE - 2)
                pygame.draw.rect(screen, self.next_tetromino.color, rect)

    def _draw_hud(self, screen):
        """Draw heads-up display"""
        hud_x = BOARD_OFFSET_X - 120
        hud_y = BOARD_OFFSET_Y + 50

        # Score
        score_label = self.font_medium.render(TEXT_SCORE, True, COLOR_TEXT_HUD)
        score_value = self.font_large.render(str(self.board.score), True, COLOR_TEXT)
        screen.blit(score_label, (hud_x, hud_y))
        screen.blit(score_value, (hud_x, hud_y + 30))

        # Level
        level_label = self.font_medium.render(TEXT_LEVEL, True, COLOR_TEXT_HUD)
        level_value = self.font_large.render(str(self.board.level), True, COLOR_TEXT)
        screen.blit(level_label, (hud_x, hud_y + 100))
        screen.blit(level_value, (hud_x, hud_y + 130))

        # Lines
        lines_label = self.font_medium.render(TEXT_LINES, True, COLOR_TEXT_HUD)
        lines_value = self.font_large.render(str(self.board.lines), True, COLOR_TEXT)
        screen.blit(lines_label, (hud_x, hud_y + 200))
        screen.blit(lines_value, (hud_x, hud_y + 230))

    def _draw_operation_hint(self, screen):
        """Draw operation hint at bottom"""
        hint_text = self.font_small.render(TEXT_OPERATION_HINT, True, COLOR_TEXT_HUD)
        hint_rect = hint_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 30))
        screen.blit(hint_text, hint_rect)

    def _draw_game_over(self, screen):
        """Draw game over overlay"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        # Game Over text
        go_text = self.font_large.render(TEXT_GAME_OVER, True, (255, 0, 0))
        go_rect = go_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        screen.blit(go_text, go_rect)

        # Score
        score_text = self.font_medium.render(f"{TEXT_FINAL_SCORE}: {self.board.score}", True, COLOR_TEXT)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(score_text, score_rect)

        # Instructions
        instruct_text = self.font_small.render(TEXT_RESTART_HINT, True, COLOR_TEXT_HUD)
        instruct_rect = instruct_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        screen.blit(instruct_text, instruct_rect)
