import cv2
from cv2 import cvtColor,imread,COLOR_RGB2GRAY, TM_CCOEFF_NORMED
import time
import numpy as np
from grab_screen import grab_screen
from rel_cords import abs2rel
from match_templat import match_templat
from set_up_board import set_up_board
from classes import Cell, BHV
from input_board import input_board
#website used on a chrome browser with book mark bar on https://sudoku.com
PYTHONBREAKPOINT = 0 # I know there is a module just don't feel like learing it right now 

# read in all refrance images
one_w=imread("./images/one_w.png",cv2.IMREAD_GRAYSCALE)
two_w=imread("./images/two_w.png",cv2.IMREAD_GRAYSCALE)
three_w=imread("./images/three_w.png",cv2.IMREAD_GRAYSCALE)
four_w=imread("./images/four_w.png",cv2.IMREAD_GRAYSCALE)
five_w=imread("./images/five_w.png",cv2.IMREAD_GRAYSCALE)
six_w=imread("./images/six_w.png",cv2.IMREAD_GRAYSCALE)
seven_w=imread("./images/seven_w.png",cv2.IMREAD_GRAYSCALE)
eight_w=imread("./images/eight_w.png",cv2.IMREAD_GRAYSCALE)
nine_w=imread("./images/nine_w.png",cv2.IMREAD_GRAYSCALE)

#bounds for a 2560 * 1600 screen top (383,380) bot (1132,1129)
#one cell is ~83.2222222222 84 pixles tall and wide 84*84
#time.sleep(1)



def any_good(listp, condtion,opprand='e'):
    for i in listp:
        if opprand == 'e':
            if i == condition:
                return True
    return False


def trim_all(board):
    for i in board:
        for obj in i:
            obj.trim(obj.box_mates , obj.h_line_mates, obj.v_line_mates)


def main():
    board_img = grab_screen(abs2rel(383,380)+abs2rel(1132,1129))
    board_img_gray = cvtColor(board_img,COLOR_RGB2GRAY)
    board = [[Cell(0,0,0,0) for col in range(9)] for row in range(9)]
    for i in range(9):
        for j in range(9): 
            obj = board[i][j]
            obj.x = i
            obj.y = j

            if i<=2 and j<=2:
                box = 0
            elif 3<=i<=5 and j<=2:
                box = 1
            elif 6<=i and j<=2:
                box = 2

            elif i<=2 and 3<=j<=5:
                box = 3
            elif 3<=i<=5 and 3<=j<=5:
                box = 4
            elif i>=6 and 3<=j<=5:
                box = 5

            elif i<=2 and j>=6:
                box = 6
            elif 3<=i<=5 and j>=6:
                box = 7
            elif i>=6 and j>=6:
                box = 8

            obj.box = box

    if False:
        while True:
            match_templat(board_img_gray,nine_w,0.85,True)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


    disp_board = [[0 for col in range(9)] for row in range(9)]
    #cant use for loop since the thresholds have to be diffrent for some numbers and nice to be able to change them indvully
    board = set_up_board(board , match_templat(board_img_gray,one_w,0.85) , 1)
    board = set_up_board(board , match_templat(board_img_gray,two_w,0.9) , 2)
    board = set_up_board(board , match_templat(board_img_gray,three_w,0.9) , 3)
    board = set_up_board(board , match_templat(board_img_gray,four_w,0.9) , 4)
    board = set_up_board(board , match_templat(board_img_gray,five_w,0.9) , 5)
    board = set_up_board(board , match_templat(board_img_gray,six_w,0.9,) , 6)
    board = set_up_board(board , match_templat(board_img_gray,seven_w,0.9) , 7)
    board = set_up_board(board , match_templat(board_img_gray,eight_w,0.9) , 8)
    board = set_up_board(board , match_templat(board_img_gray,nine_w,0.85) , 9)
    disp_board = [[0 for col in range(9)] for row in range(9)]

    # Set up the same box and line since it cannot be done when intilised
    all_box = []
    all_col = []
    all_row = []
    for i in board:
        for obj in i:
            same_box = []
            same_h_line = []
            same_v_line = []
            for comp_i in board:
                for comp_obj in comp_i:
                    # might be able to put everything under the same umbrel but nice to seprate out might be useful later
                    # will catch itself but since value is 0 does not matter
                    if obj.box == comp_obj.box:
                        same_box.append(comp_obj)

                    if obj.y == comp_obj.y:
                        same_h_line.append(comp_obj)

                    if obj.x == comp_obj.x:
                        same_v_line.append(comp_obj)
            
            obj.box_mates = same_box
            obj.h_line_mates = same_h_line
            obj.v_line_mates = same_v_line

            all_box.append(BHV(same_box))
            all_col.append(BHV(same_v_line))
            all_row.append(BHV(same_h_line))
    # group boxes and rows toghet to better find pairs that can elemi pos
    col_box_group = []

    for r in all_col:
        for pr in r.parts:
            for b in all_box:
                for pb in b.parts:
                    if pr.x == pb.x:
                        col_box_group.append([r,b])

    col_box_group = [list(t) for t in set(tuple(element) for element in col_box_group)]


    row_box_group = []

    for r in all_col:
        for pr in r.parts:
            for b in all_box:
                for pb in b.parts:
                    if pr.y == pb.y:
                        row_box_group.append([r,b])

    row_box_group = [list(t) for t in set(tuple(element) for element in row_box_group)]
    step=0
    for x in range(30):
        trim_all(board)
        for i in all_row:
            i.last_one()
        for i in all_box:
            i.last_one()
        for i in all_col:
            i.last_one()
        if x > 10:
            for i in col_box_group:
                i[0].pairs(i[0],i[1])
        if x > 15:
            for i in row_box_group:
                if i[0].genral_pair(i[0],i[1],'row'):
                    break
                '''
                for i in range(9):
                    for j in range(9):
                        disp_board[i][j] = board[j][i].value
                print(*disp_board, sep='\n')
                print(board[2][8].possibilities,'(2,8)')
                print(board[3][8].possibilities,'(3,8)')
                print(board[4][8].possibilities,'(4,8)')
                print(board[5][8].possibilities,'(5,8)')
                print(board[7][8].possibilities,'(7,8)')
                step+=1
                print(step)
                breakpoint()
                '''
                pass

                
        total=0
        for i in board:
            for j in i:
                total +=j.value
        if total == 405:
            break

    if False:
        input_board(board)


    #should proabbly fix the indexing being backordss but would have to fix it all then :(
    
    for i in range(9):
        for j in range(9):
            disp_board[i][j] = board[j][i].value
    for i in range(9):
        for j in range(9):
            disp_board[i][j] = board[j][i].value
    print(*disp_board, sep='\n')
    print(board[2][8].possibilities,'(2,8)')
    print(board[3][8].possibilities,'(3,8)')
    print(board[4][8].possibilities,'(4,8)')
    print(board[5][8].possibilities,'(5,8)')
    print(board[7][8].possibilities,'(7,8)')



if __name__ == '__main__':
    main()

