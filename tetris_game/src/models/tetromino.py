"""
Tetromino - Represents a single tetromino piece
"""

from src.constants import SHAPES, TETROMINO_COLORS


class Tetromino:
    def __init__(self, shape_type, x=0, y=0):
        self.shape_type = shape_type
        self.rotation_state = 0
        self.blocks = list(SHAPES[shape_type][self.rotation_state])
        self.color = TETROMINO_COLORS[shape_type]
        self.x = x
        self.y = y

    def get_blocks(self):
        """Get absolute block positions on the board"""
        return [(self.x + bx, self.y + by) for bx, by in self.blocks]

    def rotate(self):
        """Rotate the tetromino clockwise"""
        self.rotation_state = (self.rotation_state + 1) % 4
        self.blocks = list(SHAPES[self.shape_type][self.rotation_state])

    def rotate_back(self):
        """Rotate the tetromino counter-clockwise"""
        self.rotation_state = (self.rotation_state - 1) % 4
        self.blocks = list(SHAPES[self.shape_type][self.rotation_state])

    def move(self, dx, dy):
        """Move the tetromino by delta x and delta y"""
        self.x += dx
        self.y += dy

    def set_position(self, x, y):
        """Set absolute position"""
        self.x = x
        self.y = y

    def get_spawn_position(self, board_width):
        """Get spawn position for this tetromino type (centered at top)"""
        if self.shape_type == 'I':
            return board_width // 2 - 2, 0
        elif self.shape_type == 'O':
            return board_width // 2 - 1, 0
        else:
            return board_width // 2 - 1, 0

    def copy(self):
        """Create a deep copy of this tetromino"""
        new_tetromino = Tetromino(self.shape_type, self.x, self.y)
        new_tetromino.rotation_state = self.rotation_state
        new_tetromino.blocks = list(self.blocks)
        return new_tetromino
