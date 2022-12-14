import pygame, sys
import numpy as np

#initialize pygame
pygame.init()

#constants
WIDTH = 600
HEIGHT = 600
BG_COLOR = (28, 170, 156)
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
LINE_COLOR = ( 23, 145, 135)
CIRCLE_COLOR = ( 239, 231, 200 )
CROSS_COLOR = (66, 66, 66)
LINE_WIDTH = 15


# create screen and set size (width, height)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#title
pygame.display.set_caption( 'Tic Tac Toe Classic')
# backround color
screen.fill( BG_COLOR )

#create board
board = np.zeros( (BOARD_ROWS, BOARD_COLS))


#draw lines
#pygame.draw.line( screen, LINE_COLOR, (10, 10), (300, 300), 10)
def draw_lines():
    #horizontal line 1
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    #horizontal line 2
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    #vertical line 1
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    #vertical line 2
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

#draw circle and X
def draw_figure():
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row][col] == 1:
                #draw ascending line
                pygame.draw.line( screen, CROSS_COLOR, ( col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col*SQUARE_SIZE+SQUARE_SIZE - SPACE, row*SQUARE_SIZE+SPACE), CROSS_WIDTH)
                #draw descending line
                pygame.draw.line( screen, CROSS_COLOR, ( col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col*200+200 - SPACE, row*200+200-SPACE), CROSS_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int(row* SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH )

#mark square function
def mark_square(row, col, player):
    board[row][col] = player

#check if square is available or not
def available_square(row, col):
  return board[row][col] == 0

#check if board is full or not
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True

#check winnner
def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True

    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player)
            return True

    #ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    #descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

#draw vertical win line
def draw_vertical_win_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CROSS_COLOR
        
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), 15 )

#draw horizontal win line
def draw_horizontal_win_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), 15 )

#draw ascending diagonal win line
def draw_asc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line( screen, color, (15, HEIGHT-15), (WIDTH - 15, 15), 15)

#draw descending diagonal win line
def draw_desc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

#restart
def restart():
    screen.fill( BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False

#create a main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #check if screen is being clicked
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:


            # access x and y coordinates
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY //SQUARE_SIZE)
            clicked_col = int(mouseX //SQUARE_SIZE)

            if available_square( clicked_row, clicked_col ):
                
                mark_square( clicked_row, clicked_col, player )
                if check_win( player ):
                    game_over = True
                player = player % 2 + 1
                
                draw_figure()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
    #update screen
    pygame.display.update()