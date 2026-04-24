"""
Tetris Game Constants
"""

import pygame

# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Board settings
BOARD_WIDTH = 10  # columns
BOARD_HEIGHT = 20  # rows
CELL_SIZE = 30

# Board position
BOARD_OFFSET_X = (WINDOW_WIDTH - BOARD_WIDTH * CELL_SIZE) // 2
BOARD_OFFSET_Y = (WINDOW_HEIGHT - BOARD_HEIGHT * CELL_SIZE) // 2

# Colors
COLOR_BACKGROUND = (30, 30, 30)
COLOR_BOARD_BG = (20, 20, 20)
COLOR_GRID_LINE = (50, 50, 50)
COLOR_TEXT = (255, 255, 255)
COLOR_TEXT_HUD = (200, 200, 200)

# Tetromino colors (standard Tetris colors)
COLOR_I = (0, 255, 255)      # Cyan
COLOR_O = (255, 255, 0)      # Yellow
COLOR_T = (128, 0, 128)      # Purple
COLOR_S = (0, 255, 0)        # Green
COLOR_Z = (255, 0, 0)        # Red
COLOR_J = (0, 0, 255)        # Blue
COLOR_L = (255, 165, 0)      # Orange

TETROMINO_COLORS = {
    'I': COLOR_I,
    'O': COLOR_O,
    'T': COLOR_T,
    'S': COLOR_S,
    'Z': COLOR_Z,
    'J': COLOR_J,
    'L': COLOR_L,
}

# Tetromino shapes (each shape has 4 rotation states)
# Coordinates are relative to the center of the piece
SHAPES = {
    'I': [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (1, 1), (1, 2), (1, 3)],
        [(0, 1), (1, 1), (2, 1), (3, 1)],
        [(2, 0), (2, 1), (2, 2), (2, 3)],
    ],
    'O': [
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
    ],
    'T': [
        [(1, 0), (0, 1), (1, 1), (2, 1)],
        [(1, 0), (1, 1), (2, 1), (1, 2)],
        [(0, 1), (1, 1), (2, 1), (1, 2)],
        [(1, 0), (0, 1), (1, 1), (1, 2)],
    ],
    'S': [
        [(1, 0), (2, 0), (0, 1), (1, 1)],
        [(1, 0), (1, 1), (2, 1), (2, 2)],
        [(1, 1), (2, 1), (0, 2), (1, 2)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
    ],
    'Z': [
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(2, 0), (1, 1), (2, 1), (1, 2)],
        [(0, 1), (1, 1), (1, 2), (2, 2)],
        [(1, 0), (0, 1), (1, 1), (0, 2)],
    ],
    'J': [
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(1, 0), (2, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (2, 1), (2, 2)],
        [(1, 0), (1, 1), (0, 2), (1, 2)],
    ],
    'L': [
        [(2, 0), (0, 1), (1, 1), (2, 1)],
        [(1, 0), (1, 1), (1, 2), (2, 2)],
        [(0, 1), (1, 1), (2, 1), (0, 2)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
    ],
}

# Game settings
INITIAL_DROP_INTERVAL = 800  # milliseconds
MIN_DROP_INTERVAL = 100
LEVEL_SPEED_DECREASE = 50    # decrease interval by this much per level

# Scoring
SCORE_SINGLE = 100
SCORE_DOUBLE = 300
SCORE_TRIPLE = 500
SCORE_TETRIS = 800
LINES_PER_LEVEL = 10

# Font
FONT_NAME = 'arial'
FONT_SIZE_TITLE = 48
FONT_SIZE_LARGE = 32
FONT_SIZE_MEDIUM = 24
FONT_SIZE_SMALL = 18
