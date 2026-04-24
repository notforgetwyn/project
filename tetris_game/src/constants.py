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

# Font (use Chinese-compatible font on Windows)
FONT_NAME = 'SimHei'
FONT_SIZE_TITLE = 48
FONT_SIZE_LARGE = 32
FONT_SIZE_MEDIUM = 24
FONT_SIZE_SMALL = 18

# UI Text (Chinese, using unicode escape for safety)
TEXT_NEXT = "\u4E0B\u4E00\u4E2A"          # 下一个
TEXT_SCORE = "\u5F97\u5206"                 # 得分
TEXT_LEVEL = "\u7B49\u7EA7"                 # 等级
TEXT_LINES = "\u6D88\u884C"                 # 消行
TEXT_GAME_OVER = "\u6E38\u620F\u7ED3\u675F"  # 游戏结束
TEXT_FINAL_SCORE = "\u6700\u7EC8\u5F97\u5206"  # 最终得分
TEXT_RESTART_HINT = "\u6309 R \u91CD\u65B0\u5F00\u59CB\u6216 ESC \u8FD4\u56DE\u83DC\u5355"  # 按 R 重新开始或 ESC 返回菜单
TEXT_OPERATION_HINT = "\u2190\u2192/\u4E0D\u4E0D \u79FB\u52A8  \u2191/W \u65CB\u8F6C  \u2193/S \u52A0\u901F  \u7A7A\u683C \u786C\u964D"  # 操作提示
