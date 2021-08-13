import pygame
import os
import classes
import math

pygame.init()

SIZE = WIDTH, HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption('4line')

FPS = 1
WHITE_SQUARE = pygame.image.load(os.path.join('Assets', 'white_square.png'))
BLACK_SQUARE = pygame.image.load(os.path.join('Assets', 'black_square.png'))
PLACEHOLDER = pygame.image.load(os.path.join('Assets', 'placeholder.png'))


def draw_board():

    # Defining the 2d array which will represent the board
    board = [[]*28]*40

    # Drawing the board to the screen
    position = column, row = 100, 50
    for x in range(40):
        row = 50
        position = column, row
        for x in range(28):
            if (column + row) % 2 != 0:
                SCREEN.blit(WHITE_SQUARE, position)
            
            else: 
                SCREEN.blit(BLACK_SQUARE, position)
                
                
            row += 25
            position = column, row

        column += 25
        position = column, row

    pygame.display.update()



#Simulates placing a piece. Not added to board 2d array yet!
def place_piece():
    bool = pygame.mouse.get_pressed()
    if bool[0]:
        board_column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25)
        board_row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25)

        column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25) * 25 + 100
        row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25) * 25 + 50

        SCREEN.blit(PLACEHOLDER, (column, row))
        pygame.display.update()

        




# Main loop. Refreshes the program and calls methods.
def main():
    clock = pygame.time.Clock()
    run = True

    draw_board()

    while run:
        clock.tick(100)
        place_piece()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()