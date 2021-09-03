import pygame
import os
from classes import Piece, StartingBlock
import math
import networkx as nx
import inspect
from matplotlib import pyplot as plt

pygame.init()

SIZE = WIDTH, HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption('4line')

FPS = 1
WHITE_SQUARE = pygame.image.load(os.path.join('Assets', 'white_square.png'))
BLACK_SQUARE = pygame.image.load(os.path.join('Assets', 'black_square.png'))
PLACEHOLDER0 = pygame.image.load(os.path.join('Assets', 'circle.png'))
PLACEHOLDER1 = pygame.image.load(os.path.join('Assets', 'cross.png'))
STARTING_CROSS = pygame.image.load(os.path.join('Assets', 'starting_cross.png'))
STARTING_CIRCLE = pygame.image.load(os.path.join('Assets', 'starting_circle.png'))
CLAIMED_CIRCLE = pygame.image.load(os.path.join('Assets', 'claimed_circle.png'))
CLAIMED_CROSS = pygame.image.load(os.path.join('Assets', 'claimed_cross.png'))

def start_screen():
    pass





# Defining the 2d array which will represent the board

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
]

board_graph = nx.Graph()



def draw_board():

    # Drawing the board to the screen
    position = column, row = 100, 50
    for x in range(40):
        row = 50
        position = column, row
        for y in range(28):
            if (column + row) % 2 != 0 and board[x][y] == 0:
                SCREEN.blit(WHITE_SQUARE, position)
            
            elif (column + row) % 2 == 0 and board[x][y] == 0: 
                SCREEN.blit(BLACK_SQUARE, position)
                   
            row += 25
            position = column, row

        column += 25
        position = column, row

    pygame.display.update()

def update_board():
    for x in range(40):
        for y in range(28):
            if board[x][y] == 0:
                if (x + y) % 2 != 0 and board[x][y] == 0:
                    SCREEN.blit(WHITE_SQUARE, (x * 25 + 100, y * 25 + 50))
            
                elif (x + y) % 2 == 0 and board[x][y] == 0: 
                    SCREEN.blit(BLACK_SQUARE, (x * 25 + 100, y * 25 + 50))
            
            

    pygame.display.update()


def select_start():
    start_blocks = []
    player = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bool = pygame.mouse.get_pressed()
        if bool[0]:
            board_column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25)
            board_row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25)

            column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25) * 25 + 100
            row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25) * 25 + 50



            if board_column >= 15 and board_row >= 9:
                if board_column < 26 and board_row < 20:
                    if board[board_column][board_row] == 0:
                        if player == 0:
                            SCREEN.blit(STARTING_CIRCLE, (column, row))
                            board[board_column][board_row] = StartingBlock(player)
                            pygame.display.update()
                            start_blocks.append((board_column, board_row))
                            board_graph.add_node((board_column, board_row))
                        else:
                            SCREEN.blit(STARTING_CROSS, (column, row))
                            board[board_column][board_row] = StartingBlock(player)
                            pygame.display.update()
                            start_blocks.append((board_column, board_row))
                            board_graph.add_node((board_column, board_row))
                            return start_blocks
                        player = 1
                    



#Places a piece onto the screen. checks if action can be done and if yes places the placeholder according to the current_player. If action is succesfull changes the player.
def place_piece(player, piece_placed, available_moves, move, special_moves):
    if available_moves > 0:
        bool = pygame.mouse.get_pressed()
        if bool[0]:
            board_column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25)
            board_row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25)

            column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25) * 25 + 100
            row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25) * 25 + 50

            #Checks if the coordinates are in the available range and if a piece has net yet been placed in that location, places a piece
            if board_column >= 0 and board_row >= 0:
                if board_column < 40 and board_row < 28:
                    if board[board_column][board_row] == 0:
                        valid, move = check_move((board_column, board_row), move, player)
                        if valid:
                            # Places the square and switches the current player
                            if player == 0:
                                SCREEN.blit(PLACEHOLDER0, (column, row))
                                board[board_column][board_row] = Piece(player)
                                pygame.display.update()
                                piece_placed = True
                                available_moves -= 1
                                return piece_placed, available_moves, move, special_moves
                            else:
                                SCREEN.blit(PLACEHOLDER1, (column, row))
                                board[board_column][board_row] = Piece(player)
                                pygame.display.update()
                                piece_placed = True
                                available_moves -= 1
                                return piece_placed, available_moves, move, special_moves


    elif special_moves > 0:
        bool = pygame.mouse.get_pressed()
        if bool[0]:
            board_column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25)
            board_row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25)

            column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25) * 25 + 100
            row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25) * 25 + 50

            #Checks if the coordinates are in the available range and if a piece has net yet been placed in that location, places a piece
            if board_column >= 0 and board_row >= 0:
                if board_column < 40 and board_row < 28:
                    if board[board_column][board_row] == 0:
                        valid, move = check_move((board_column, board_row), move, player)
                        if valid:
                            # Places the square and switches the current player
                            if player == 0:
                                SCREEN.blit(PLACEHOLDER0, (column, row))
                                board[board_column][board_row] = Piece(player)
                                pygame.display.update()
                                piece_placed = True
                                special_moves -= 1
                                return piece_placed, available_moves, move, special_moves
                            else:
                                SCREEN.blit(PLACEHOLDER1, (column, row))
                                board[board_column][board_row] = Piece(player)
                                pygame.display.update()
                                piece_placed = True
                                special_moves -= 1
                                return piece_placed, available_moves, move, special_moves

    # If button not pressed or invalid piece placement, player remains the same.
    return piece_placed, available_moves, move, special_moves



# checks if a certain move is valid, namely whether a placeholder will sit next to another placeholder
def check_move(position, move, player):

    valid = False
    valid_counter = 0

    #Try and except statements are in place so as not to get a list index out of range error when checking a move on the 40th column or 28th row
    try:
        if move < 2:
            is_start = isinstance(board[position[0] + 1][position[1]], StartingBlock)
            if is_start:
                valid = player == board[position[0] + 1][position[1]].team
        else:
            valid = board[position[0] + 1][position[1]] != 0

        if valid:

            board_graph.add_edge((position[0] + 1, position[1]),(position[0],position[1]))
            valid_counter += 1
            valid = False

    except:
        pass
    try: 
        if move < 2:
            is_start = isinstance(board[position[0] - 1][position[1]], StartingBlock)
            if is_start:
                valid = player == board[position[0] - 1][position[1]].team
        else:
            valid = board[position[0] - 1][position[1]] != 0
        if valid: 
            board_graph.add_edge((position[0] - 1, position[1]),(position[0],position[1]))
            valid_counter += 1
            valid = False


    except:
        pass
    try:
        if move < 2:
            is_start = isinstance(board[position[0]][position[1] + 1], StartingBlock)
            if is_start:
                valid = player == board[position[0]][position[1] + 1].team
        else:
            valid = board[position[0]][position[1] + 1] != 0
        if valid:
            board_graph.add_edge((position[0], position[1] + 1),(position[0],position[1]))
            valid_counter += 1
            valid = False

    except:
        pass

    if move < 2:
        is_start = isinstance(board[position[0]][position[1] - 1], StartingBlock)
        if is_start:
            valid = player == board[position[0]][position[1] - 1].team
    else:
        valid = board[position[0]][position[1] - 1] != 0
    if valid:
        board_graph.add_edge((position[0], position[1] - 1),(position[0],position[1]))
        valid_counter += 1
        valid = False


    if valid_counter > 0:
        move += 1
        return True, move
    else:
        return False, move

def claim_line(player, selected_blocks, available_moves, special_moves):
    bool = pygame.mouse.get_pressed()
    if bool[2]:
        board_column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25)
        board_row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25)
        if board_column >= 0 and board_row >= 0:
            if board_column < 40 and board_row < 28:
                for x in selected_blocks[player]:
                     if x == (board_column, board_row):
                         return selected_blocks, available_moves, special_moves

                if board[board_column][board_row] == 0:
                    return selected_blocks, available_moves, special_moves

                if board[board_column][board_row].team != player:
                    return selected_blocks, available_moves, special_moves
                
                selected_blocks[player].append((board_column, board_row))
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        selected_blocks[player].clear()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        #First check a vertical solve
        
        if len(selected_blocks[player]) != 4:
            selected_blocks[player].clear()
            return selected_blocks, available_moves, special_moves

        column_nums = []
        row_nums = []
        valid_claim = False

        for tuple in selected_blocks[player]:
            column_nums.append(tuple[0])
            row_nums.append(tuple[1])

        for index in range(len(column_nums)):
            if column_nums[index] == column_nums[index - 1]:
                valid = True
                continue

            else:
                valid = False
                break

        if valid:
            row_nums.sort()
            for index in range(len(row_nums)):
                if index == len(row_nums) - 1:
                    break
                if row_nums[index] + 1 == row_nums[index + 1]:
                    valid_claim = True
        
        if valid_claim:
            for tuple in selected_blocks[player]:
                if player == 0:
                    SCREEN.blit(CLAIMED_CIRCLE, (tuple[0] * 25 + 100, tuple[1] * 25 + 50))
                    pygame.display.update()
                else:
                    SCREEN.blit(CLAIMED_CROSS, (tuple[0] * 25 + 100, tuple[1] * 25 + 50))
                    pygame.display.update()

                board[tuple[0]][tuple[1]].status = True


            selected_blocks[player].clear()
            return selected_blocks, available_moves, special_moves



        #Then check for a horizontal one
        column_nums = []
        row_nums = []
        valid_claim = False

        for tuple in selected_blocks[player]:
            column_nums.append(tuple[0])
            row_nums.append(tuple[1])

        for index in range(len(row_nums)):
            if row_nums[index] == row_nums[index - 1]:
                valid = True
                continue

            else:
                valid = False
                break

        if valid:
            column_nums.sort()
            for index in range(len(column_nums)):
                if index == len(column_nums) - 1:
                    break
                if column_nums[index] + 1 == column_nums[index + 1]:
                    valid_claim = True
                else: 
                    return selected_blocks, available_moves, special_moves
        
        if valid_claim:
            for tuple in selected_blocks[player]:
                if player == 0:
                    SCREEN.blit(CLAIMED_CIRCLE, (tuple[0] * 25 + 100, tuple[1] * 25 + 50))
                    pygame.display.update()
                else:
                    SCREEN.blit(CLAIMED_CROSS, (tuple[0] * 25 + 100, tuple[1] * 25 + 50))
                    pygame.display.update()

                board[tuple[0]][tuple[1]].status = True
            
            selected_blocks[player].clear()
            return selected_blocks, available_moves, special_moves

            

            #Now time to check any diagonals

        column_nums = []
        row_nums = []
        valid_claim = False

        for tuple in selected_blocks[player]:
            column_nums.append(tuple[0])
            row_nums.append(tuple[1])
        
        row_nums.sort()
        column_nums.sort()

        for index in range(len(row_nums)):
            if index == len(row_nums) - 1:
                    break


            if  row_nums[index] + 1 == row_nums[index + 1]:
                valid = True
                continue

            else:
                valid = False
                break


        if valid:
            for index in range(len(column_nums)):
                if index == len(column_nums) - 1:
                    break
                if column_nums[index] + 1 == column_nums[index + 1]:
                    valid_claim = True
                else: 
                    return selected_blocks, available_moves, special_moves
        
        if valid_claim:
            for tuple in selected_blocks[player]:
                if player == 0:
                    SCREEN.blit(CLAIMED_CIRCLE, (tuple[0] * 25 + 100, tuple[1] * 25 + 50))
                    pygame.display.update()
                else:
                    SCREEN.blit(CLAIMED_CROSS, (tuple[0] * 25 + 100, tuple[1] * 25 + 50))
                    pygame.display.update()

                board[tuple[0]][tuple[1]].status = True
            
            selected_blocks[player].clear()
            return selected_blocks, available_moves, special_moves


            #Now time to check if a square hass been claimed

        column_nums = []
        row_nums = []
        valid_claim = False

        for tuple in selected_blocks[player]:
            column_nums.append(tuple[0])
            row_nums.append(tuple[1])
        
        row_nums.sort()
        column_nums.sort()

        for index in range(len(row_nums)):
            if index == 1 or index == 3:
                    break

            if index == 0 or index == 2:
                if  row_nums[index] == row_nums[index + 1]:
                    valid = True
                    continue

                else:
                    valid = False
                    break


        if valid:
            for index in range(len(column_nums)):
                if index == 1 or index == 3:
                    break

                if index == 0 or index == 2:
                    if  column_nums[index] == column_nums[index + 1]:
                        valid_claim = True
                else: 
                    return selected_blocks, available_moves, special_moves
        
        if valid_claim:
            available_moves += 1
            special_moves += 1
            for tuple in selected_blocks[player]:
                if player == 0:
                    SCREEN.blit(CLAIMED_CIRCLE, (tuple[0] * 25 + 100, tuple[1] * 25 + 50))
                    pygame.display.update()
                else:
                    SCREEN.blit(CLAIMED_CROSS, (tuple[0] * 25 + 100, tuple[1] * 25 + 50))
                    pygame.display.update()

                board[tuple[0]][tuple[1]].status = True
            
            selected_blocks[player].clear()
            return selected_blocks, available_moves, special_moves

        
    return selected_blocks, available_moves, special_moves






def change_player(player, piece_placed, available_moves, special_moves):
    new_player = player
    if piece_placed and available_moves == 0 and special_moves == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if player == 0:
                new_player = 1
                piece_placed = False
                available_moves += 1
            else:
                new_player = 0
                piece_placed = False
                available_moves += 1
    

    return new_player, piece_placed, available_moves
        
def delete_piece(start_blocks, special_moves, piece_placed):
    remove = True
    all_islands = []
    bool = pygame.mouse.get_pressed()
    if special_moves > 0:

        if bool[1]:
            board_column = math.floor((pygame.mouse.get_pos()[0] - 100) / 25)
            board_row = math.floor((pygame.mouse.get_pos()[1] - 50) / 25)

            if isinstance(board[board_column][board_row], Piece):
                print('Debug 1')
                claimed = board[board_column][board_row].status
                print(claimed)
                if claimed:
                    return special_moves, piece_placed

            try:
                board_graph.remove_node((board_column, board_row))
                board[board_column][board_row] = 0
                special_moves -= 1
                piece_placed = True
            except:
                pass

            
            for island in nx.connected_components(board_graph):
                all_islands.append(island)


            for island in all_islands:
                if start_blocks[0] in island:
                    remove = False
                elif start_blocks[1] in island: 
                    remove = False
                else:
                    remove = True

                if remove:
                    for node in island:
                        board_graph.remove_node((node))
                        board[node[0]][node[1]] = 0

    
    update_board()
    return special_moves, piece_placed

        




# Main loop. Refreshes the program and calls methods.
def main():
    move = 0
    clock = pygame.time.Clock()
    run = True
    player = 0
    special_moves = 0
    available_moves = 1
    selected_blocks = [[],[]]
    piece_placed = False
    draw_board()
    start_blocks = select_start()

    while run:
        clock.tick(60)
        piece_placed, available_moves, move, special_moves = place_piece(player, piece_placed, available_moves, move, special_moves)
        selected_blocks, available_moves, special_moves = claim_line(player, selected_blocks, available_moves, special_moves)
        player, piece_placed, available_moves = change_player(player, piece_placed, available_moves, special_moves)
        special_moves, piece_placed = delete_piece(start_blocks, special_moves, piece_placed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    nx.draw(board_graph)
    plt.show()

if __name__ == "__main__":
    main()