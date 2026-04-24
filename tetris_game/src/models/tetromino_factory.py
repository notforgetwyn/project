"""
TetrominoFactory - Creates random tetromino pieces
"""

import random
from src.models.tetromino import Tetromino


class TetrominoFactory:
    SHAPE_TYPES = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']

    def __init__(self):
        self.bag = []
        self._refill_bag()

    def _refill_bag(self):
        """Refill the bag with all 7 tetromino types (random shuffle)"""
        self.bag = list(self.SHAPE_TYPES)
        random.shuffle(self.bag)

    def create_tetromino(self, shape_type):
        """Create a specific tetromino type"""
        return Tetromino(shape_type)

    def get_random_tetromino(self):
        """Get a random tetromino from the bag"""
        if not self.bag:
            self._refill_bag()
        shape_type = self.bag.pop()
        return Tetromino(shape_type)
