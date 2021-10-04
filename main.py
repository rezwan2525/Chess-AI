import pygame
from pygame.locals import * # store value to pygame locals
import sys
from colors import *
from board import Board
from constants import *
from board_utility import *
from piece import *

pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()


SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Chess AI")


chess_board = Board(SCREEN )

all_pieces = pygame.sprite.Group()

for i in range(0,len(piece_init_pos)):
    for j in range(0,len(piece_init_pos[i])):
        # i is index towards x-axis , whereas j is index towards y-axis
        if isPiece(piece_init_pos[i][j]):
            image_path = 'images/'+piece_init_pos[i][j]+'.png'
            temp_piece = Piece(image_path)
            print(i,j)
            temp_piece.set_center(coordinate_to_center_pixel(j,i))
            all_pieces.add(temp_piece)

while True:
    # codes here
    
    
    pygame.display.update()
    chess_board.draw()
    all_pieces.draw(SCREEN)

    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            print("Clcikecd:    ", str(pygame.mouse.get_pos()))
            print(pixel_to_coordinate(*pygame.mouse.get_pos()))    
    #pygame.display.flip()
    FramePerSec.tick(FPS)