import pygame

ROW , COLUMN = 8, 4
SCREEN_HEIGHT, SCREEN_WIDTH = 720, 360
TILE_HEIGHT, TILE_WIDTH = int(SCREEN_HEIGHT/ ROW) , int(SCREEN_WIDTH/COLUMN)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

WHITE_QUEEN = 'wQ'
WHITE_KING = 'wK'
WHITE_PAWN = 'wP'
WHITE_ROOK = 'wR'

BLACK_QUEEN = 'bQ'
BLACK_KING = 'bK'
BLACK_PAWN = 'bP'
BLACK_ROOK = 'bR'
EMPTY_PIECE = 'E'


all_piece_pos = [
    [WHITE_ROOK,     WHITE_QUEEN,     WHITE_KING,     WHITE_ROOK],
    [WHITE_PAWN,     WHITE_PAWN,      WHITE_PAWN,     WHITE_PAWN],
    [EMPTY_PIECE,    EMPTY_PIECE,     EMPTY_PIECE,    EMPTY_PIECE],
    [EMPTY_PIECE,    EMPTY_PIECE,     EMPTY_PIECE,    EMPTY_PIECE],
    [EMPTY_PIECE,    EMPTY_PIECE,     EMPTY_PIECE,    EMPTY_PIECE],
    [EMPTY_PIECE,    EMPTY_PIECE,     EMPTY_PIECE,    EMPTY_PIECE],
    [BLACK_PAWN,     BLACK_PAWN,      BLACK_PAWN,      BLACK_PAWN],
    [BLACK_ROOK,     BLACK_KING,      BLACK_QUEEN,     BLACK_ROOK],
]
