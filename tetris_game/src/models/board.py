"""
Board - Represents the game board and handles line clearing
"""

from src.constants import (
    BOARD_WIDTH, BOARD_HEIGHT, SCORE_SINGLE, SCORE_DOUBLE,
    SCORE_TRIPLE, SCORE_TETRIS, LINES_PER_LEVEL
)


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.lines = 0
        self.level = 1

    def is_inside_board(self, x, y):
        """Check if position is inside the board boundaries"""
        return 0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT

    def is_empty(self, x, y):
        """Check if a cell is empty"""
        if not self.is_inside_board(x, y):
            return False
        return self.grid[y][x] is None

    def is_collision(self, tetromino):
        """Check if tetromino collides with board boundaries or locked pieces"""
        for bx, by in tetromino.get_blocks():
            if not self.is_inside_board(bx, by):
                return True
            if not self.is_empty(bx, by):
                return True
        return False

    def lock_tetromino(self, tetromino):
        """Lock a tetromino onto the board"""
        for bx, by in tetromino.get_blocks():
            if self.is_inside_board(bx, by):
                self.grid[by][bx] = tetromino.color

    def clear_lines(self):
        """Clear completed lines and return the number of lines cleared"""
        lines_to_clear = []

        for y in range(BOARD_HEIGHT):
            if all(self.grid[y][x] is not None for x in range(BOARD_WIDTH)):
                lines_to_clear.append(y)

        if not lines_to_clear:
            return 0

        # Remove cleared lines
        for line_y in lines_to_clear:
            del self.grid[line_y]
            self.grid.insert(0, [None for _ in range(BOARD_WIDTH)])

        # Update score based on lines cleared
        num_lines = len(lines_to_clear)
        if num_lines == 1:
            self.score += SCORE_SINGLE
        elif num_lines == 2:
            self.score += SCORE_DOUBLE
        elif num_lines == 3:
            self.score += SCORE_TRIPLE
        else:
            self.score += SCORE_TETRIS

        # Update total lines and level
        self.lines += num_lines
        new_level = self.lines // LINES_PER_LEVEL + 1
        if new_level > self.level:
            self.level = new_level

        return num_lines

    def is_game_over(self):
        """Check if the top rows are occupied (game over condition)"""
        for x in range(BOARD_WIDTH):
            if self.grid[0][x] is not None:
                return True
        return False

    def can_spawn(self, tetromino):
        """Check if a tetromino can be spawned at its position"""
        return not self.is_collision(tetromino)

    def reset(self):
        """Reset the board to initial state"""
        self.grid = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.lines = 0
        self.level = 1

    def get_drop_interval(self, initial_interval, min_interval, decrease_per_level):
        """Calculate drop interval based on level"""
        interval = initial_interval - (self.level - 1) * decrease_per_level
        return max(interval, min_interval)
