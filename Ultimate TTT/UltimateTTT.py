#! "C:\Users\BING BING\Desktop\Projects\Python Projects\myenv\Scripts\python.exe"
import pygame as pg, sys
import math
from Button import Button 

pg.init()
# all the initial variables
WIDTH, HEIGHT = 720, 820
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe!")
BIG_BOARD = pg.image.load("assets/Board.png")
BIG_X = pg.image.load("assets/X.png")
BIG_O = pg.image.load("assets/O.png")
BIG_BOARD = pg.transform.scale(BIG_BOARD,(720,720))
SMALL_BOARD = pg.transform.scale(BIG_BOARD,(240,240))
SMALL_ACTIVE_BOARD = pg.transform.scale(pg.image.load("assets/Board_Active.png"),(240,240))
SMALL_X = pg.transform.scale(BIG_X,(round(BIG_X.get_height()/3),round(BIG_X.get_width()/3)))
SMALL_O = pg.transform.scale(BIG_O,(round(BIG_O.get_height()/3),round(BIG_O.get_width()/3)))
BG_COLOR = (200, 200, 200)

def initialize_game():
    
    board = [ [ [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ] ] , [ [ 10 , 11 , 12 ] , [ 13 , 14 , 15 ] , [ 16 , 17 , 18 ] ] , [ [ 19 , 20 , 21 ] , [ 22 , 23 , 24 ] , [ 25 , 26 , 27 ] ] ] ,
            [ [ [ 28 , 29 , 30 ] , [ 31 , 32 , 33 ] , [ 34 , 35 , 36 ] ] , [ [ 37 , 38 , 39 ] , [ 40 , 41 , 42 ] , [ 43 , 44 , 45 ] ] , [ [ 46 , 47 , 48 ] , [ 49 , 50 , 51 ] , [ 52 , 53 , 54 ] ] ] ,
            [ [ [ 55 , 56 , 57 ] , [ 58 , 59 , 60 ] , [ 61 , 62 , 63 ] ] , [ [ 64 , 65 , 66 ] , [ 67 , 68 , 69 ] , [ 70 , 71 , 72 ] ] , [ [ 73 , 74 , 75 ] , [ 76 , 77 , 78 ] , [ 79 , 80 , 81 ] ] ] ] 
    graphical_board = [ [ [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] ] , 
                        [ [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] ] , 
                        [ [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] ] ] 
    big_board = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ] ]
    big_graphical_board = [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] 
    active_box =[None, None]
    text_font = pg.font.Font("assets/font.ttf", 30)
    turn = 'X'
    game_finished = False

    return board,graphical_board,big_board,big_graphical_board,active_box,text_font,turn,game_finished

def get_font(size):
    return pg.font.Font("assets/font.ttf", size)

def draw_text(text, font, text_col):
    img = font.render(text,font, text_col)
    x = (720 - img.get_width())/2
    y = 750
    SCREEN.blit(img,(x,y))

def newGame():

    board = [ [ [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ] ] , [ [ 10 , 11 , 12 ] , [ 13 , 14 , 15 ] , [ 16 , 17 , 18 ] ] , [ [ 19 , 20 , 21 ] , [ 22 , 23 , 24 ] , [ 25 , 26 , 27 ] ] ] ,
            [ [ [ 28 , 29 , 30 ] , [ 31 , 32 , 33 ] , [ 34 , 35 , 36 ] ] , [ [ 37 , 38 , 39 ] , [ 40 , 41 , 42 ] , [ 43 , 44 , 45 ] ] , [ [ 46 , 47 , 48 ] , [ 49 , 50 , 51 ] , [ 52 , 53 , 54 ] ] ] ,
            [ [ [ 55 , 56 , 57 ] , [ 58 , 59 , 60 ] , [ 61 , 62 , 63 ] ] , [ [ 64 , 65 , 66 ] , [ 67 , 68 , 69 ] , [ 70 , 71 , 72 ] ] , [ [ 73 , 74 , 75 ] , [ 76 , 77 , 78 ] , [ 79 , 80 , 81 ] ] ] ] 
    graphical_board = [ [ [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] ] , 
                        [ [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] ] , 
                        [ [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] , [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] ] ] 
    big_board = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ] ]
    big_graphical_board = [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] 
    active_box =[None, None]
    turn = 'X'

    return big_board, big_graphical_board, board, graphical_board, active_box, turn

def reset_box(board, graphical_board):
    board = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9 ] ]
    graphical_board = [ [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] , [ [None, None], [None, None], [None, None]] ] 
    return board, graphical_board

def check_win3x3(board):
    winner = None
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            return winner
 
    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        return winner
    
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O' and board[i][j]!= "DRAW":
                    return None
        return "DRAW"
    
def check_win(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font):

    # checking the small win
    for i in range(3):
        for j in range(3):
            if big_board[i][j] != 'X' and big_board[i][j] != 'O':
                if check_win3x3(board[i][j]) is not None:
                    big_board[i][j] = check_win3x3(board[i][j])
                    if big_board[i][j] == 'X' or big_board[i][j] == 'O':
                        board[i][j], graphical_board[i][j] =reset_box(board[i][j],graphical_board[i][j])
                        update_screen(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font)
                        

    return check_win3x3(big_board)

def render_board(big_board, big_graphical_board, board,graphical_board, ximg, oimg):
    for i in range(3):
        for j in range(3):
            
            if big_board[i][j] =='X':
                big_graphical_board[i][j][0] = BIG_X
                big_graphical_board[i][j][1] = BIG_X.get_rect(center = (i*240+120,j*240+120))
            if big_board[i][j] =='O':
                big_graphical_board[i][j][0] = BIG_O
                big_graphical_board[i][j][1] = BIG_O.get_rect(center = (i*240+120,j*240+120))

            for k in range(3):
                for l in range(3):
                    if board[i][j][k][l] =='X':
                        graphical_board[i][j][k][l][0] = ximg
                        graphical_board[i][j][k][l][1] = ximg.get_rect(center= (i*240 + 40 + (k*80),j*240  +40+(l*80)))
                    elif board[i][j][k][l] =='O':
                        graphical_board[i][j][k][l][0] = oimg
                        graphical_board[i][j][k][l][1] = oimg.get_rect(center= (i*240 + 40 + (k*80),j*240  +40+(l*80)))

    return big_graphical_board, graphical_board

def add_XO(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font):
    curr_pos = pg.mouse.get_pos()
    converted_x = math.floor((curr_pos[0])/240)
    converted_y = math.floor((curr_pos[1])/240)
    converted_z = math.floor((curr_pos[0])%240/80)
    converted_a = math.floor((curr_pos[1])%240/80)
    
    if converted_a < 3 and converted_y <3 and converted_z < 3 and converted_a <3 and (active_box[0]is None or (converted_x == active_box[0] and converted_y == active_box[1])) and big_board[converted_x][converted_y] != 'O' and big_board[converted_x][converted_y] != 'X' and board[converted_x][converted_y][converted_z][converted_a]!= 'O' and board[converted_x][converted_y][converted_z][converted_a]!= 'X':
        board[converted_x][converted_y][converted_z][converted_a]= turn
        if turn =='O':
            turn ='X'
        else:
            turn ='O'
            
        game_finished = check_win(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font)

        if big_board[converted_z][converted_a] == 'X' or big_board[converted_z][converted_a] == 'O' or big_board[converted_z][converted_a] == 'DRAW' or game_finished is not None:
            active_box = [None, None]
        else:
            active_box = [converted_z, converted_a]
    

    big_graphical_board, graphical_board = render_board(big_board, big_graphical_board, board,graphical_board,SMALL_X,SMALL_O)
    
    return big_board, big_graphical_board, board,graphical_board, turn, active_box           


def update_screen(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font):
    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BIG_BOARD, (0, 0))
    for i in range(3):
        for j in range (3):
            if big_board[i][j] != 'X' and big_board[i][j] != 'O':
                pos_x =  i*240
                pos_y =  j*240
                if active_box == [i,j] and game_finished == False:
                    SCREEN.blit(SMALL_ACTIVE_BOARD,(pos_x,pos_y))
                else:
                    SCREEN.blit(SMALL_BOARD,(pos_x,pos_y))

    for i in range(3):
        for j in range(3):
            
            if big_graphical_board[i][j][0] is not None:
                SCREEN.blit(big_graphical_board[i][j][0],big_graphical_board[i][j][1])

            for k in range(3):
                for l in range(3):
                    if graphical_board[i][j][k][l][0] is not None:
                        SCREEN.blit(graphical_board[i][j][k][l][0],graphical_board[i][j][k][l][1])
    pg.draw.line(SCREEN,(0,0,0),(0,720),(720,720),width=5)

   
    if check_win(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font) is None:
        draw_text(f"{turn}'s Turn", text_font, (0,0,0))
    else:
        if check_win(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font) == "DRAW":
            draw_text("Draw!(Click To Replay)", text_font, (0,0,0))
        else:
            draw_text(f"{check_win(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font)} Win!(Click to Replay)", text_font, (0,0,0))

    # back_Button = Button(None,(690,735),"BACK",get_font(13),"red","black")
    # curr_pos = pg.mouse.get_pos()
    # back_Button.changeColor(curr_pos)
    # back_Button.update(SCREEN)
    pg.display.update()

    




# main menu
pg.mixer.music.load("assets/BG Music.mp3")
pg.mixer.music.set_volume(0.05)
pg.mixer.music.play(-1,0,300)

def play_menu():

    board,graphical_board,big_board,big_graphical_board,active_box,text_font,turn,game_finished = initialize_game()
    update_screen(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font)

    


    while True:
        curr_pos = pg.mouse.get_pos()
        back_Button = Button(None,(690,735),"BACK",get_font(13),"red","black")
        back_Button.changeColor(curr_pos)
        back_Button.update(SCREEN)
        pg.display.update()


        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                
                if back_Button.checkForInput(curr_pos):
                    main_menu()

                big_board, big_graphical_board, board,graphical_board, turn, active_box = add_XO(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font)
                update_screen(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font)


                if game_finished == True:
                    big_board, big_graphical_board, board, graphical_board, active_box, turn = newGame()
                    update_screen(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font)
                    game_finished = False

                if  check_win(big_board, big_graphical_board,board, graphical_board, turn, active_box,game_finished, text_font) is not None:
                    game_finished = True
                    big_board, big_graphical_board, board, graphical_board, active_box, turn = newGame()
                
                

def main_menu():
    while True:
        SCREEN.fill(BG_COLOR)

        curr_pos = pg.mouse.get_pos()

        menu_text = get_font(60).render("ULTIMATE", True, "#2589BD")
        menu_rect = menu_text.get_rect(center=(360,100))        
        SCREEN.blit(menu_text,menu_rect)        
        menu_text = get_font(60).render("TIC TAC TOE", True, "#2589BD")
        menu_rect = menu_text.get_rect(center=(360,200))
        SCREEN.blit(menu_text,menu_rect)


        play_Button = Button(None,(360,400),"PLAY",get_font(50),"#2589BD","#00466B" )
        exit_Button = Button(None,(360,500),"EXIT",get_font(50),"#2589BD","#00466B" )




        for button in [play_Button,exit_Button]:
            button.changeColor(curr_pos)
            button.update(SCREEN)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if play_Button.checkForInput(curr_pos):
                    play_menu()
                if exit_Button.checkForInput(curr_pos):
                    pg.quit()
                    sys.exit()                  

        pg.display.update()


main_menu()




