import cv2
from cv2 import cvtColor,imread,COLOR_RGB2GRAY, TM_CCOEFF_NORMED
import time
import numpy as np
from grab_screen import grab_screen
from rel_cords import abs2rel
from match_templat import match_templat
from set_up_board import set_up_board
from classes import Cell, BHV
from input_board import input_board,show_possibilities
import copy
#website used on a chrome browser with book mark bar on https://sudoku.com
PYTHONBREAKPOINT = 0 # I know there is a module just don't feel like learing it right now 

# read in all refrance images
one_w = imread("./images/one_w.png",cv2.IMREAD_GRAYSCALE)
two_w = imread("./images/two_w.png",cv2.IMREAD_GRAYSCALE)
three_w = imread("./images/three_w.png",cv2.IMREAD_GRAYSCALE)
four_w = imread("./images/four_w.png",cv2.IMREAD_GRAYSCALE)
five_w = imread("./images/five_w.png",cv2.IMREAD_GRAYSCALE)
six_w = imread("./images/six_w.png",cv2.IMREAD_GRAYSCALE)
seven_w = imread("./images/seven_w.png",cv2.IMREAD_GRAYSCALE)
eight_w = imread("./images/eight_w.png",cv2.IMREAD_GRAYSCALE)
nine_w = imread("./images/nine_w.png",cv2.IMREAD_GRAYSCALE)

#bounds for a 2560 * 1600 screen top (383,380) bot (1132,1129)
#one cell is ~83.2222222222 84 pixles tall and wide 84*84
#time.sleep(2)


def any_good(listp, condtion, opprand='e'):
    for i in listp:
        if opprand == 'e':
            if i == condition:
                return True
    return False


def trim_all(board):
    for i in board:
        for obj in i:
            obj.trim(obj.box_mates , obj.h_line_mates, obj.v_line_mates)


def genral_pair(line,boxs,line_type):                
    for need in line.needs:
        can = []
        for part in line.parts:
            for pos in part.possibilities:
                if pos == need:
                    can.append(part)

        if len(can)>1:
            all_con = []
            for i in can:
                if i.box == can[0].box:
                    all_con.append(True)
                else:
                    all_con.append(False)

            if all(all_con):
                #print('enter')
                remove_from = []

                if line_type == 'col':
                    y = can[0].y  
                    if 0 <= y and y < 3:
                        remove_box = boxs[0]
                    elif 3 <= y and y < 6:
                        remove_box = boxs[1]
                    else:
                        remove_box = boxs[2]
                elif line_type == 'row':
                    x = can[0].x
                    if 0 <= x and x <= 2:
                        remove_box = boxs[0]
                    elif 3 <= x and x <= 5:
                        remove_box = boxs[1]
                    else:
                        remove_box = boxs[2]

                    for i in remove_box.parts:
                        if line_type == 'col':
                            if i.x != line.parts[0].x and i.value == 0:
                                remove_from.append(i)
                        elif line_type == 'row':
                            if i.y != line.parts[0].y and i.value == 0:
                                remove_from.append(i)

            
                for i in remove_from:
                    #print('line x', line.parts[0].x,'need', need)
                    #print('removeing',need,'from', f'({i.x},{i.y})')
                    i.possibilities = np.delete(i.possibilities, np.where(i.possibilities == need))


def trip_pair(boxs):
    for box in boxs:
        can = []
        if len(box.needs)>3:
            for i in box.parts:
                if len(i.possibilities) <= 3:
                    can.append(i)
            # time for some really stupitiy
            '''
            for check_aginest in range(123,987):
                # will give a int 123 to check pair one two three then 124 359 ect to check all pairs probly dont need to go two 987 but what ever
                # I swear I could use genrators or something to do this better with any() but I dont know how to do that currentlly
                pair_up = []
            '''
            for master in range(123,987):
                pair_up = []
                '''
                for i in can:
                    if len(i.possibilities) == 3:
                        master = i.possibilities # know it is a term for severs figth me
                        #print(master)
                        break
                '''
                for i in can:
                    simlarity = 0
                    for pos in i.possibilities:
                        if pos == int(str(master)[0]) and int(str(master)[0]) != int(str(master)[1]) and int(str(master)[0]) != int(str(master)[2]) and int(str(master)[1]) != int(str(master)[2]):
                            simlarity += 1
                        if pos ==  int(str(master)[1]) and int(str(master)[0]) != int(str(master)[1]) and int(str(master)[0]) != int(str(master)[2]) and int(str(master)[1]) != int(str(master)[2]):
                            simlarity += 1
                        if pos ==  int(str(master)[2]) and int(str(master)[0]) != int(str(master)[1]) and int(str(master)[0]) != int(str(master)[2]) and int(str(master)[1]) != int(str(master)[2]):
                            simlarity += 1

                        if (simlarity == 2 and len(i.possibilities) == 2) or (simlarity == 3 and len(i.possibilities == 3)):
                            pair_up.append(i)

                if len(pair_up) == 3:
                    #print(master,'nice box',pair_up[0].box, pair_up[0].possibilities,pair_up[1].possibilities,pair_up[2].possibilities)
                    for remove in str(master):
                        for part in box.parts:
                            condtions = []
                            for not_this in pair_up:
                                if part != not_this:
                                    condtions.append(True)
                                else:
                                    condtions.append(False)
                            if all(condtions):
                                part.remove_pos(int(remove))
                                #print('removeing', remove, 'from',f'({part.x},{part.y})')
                            
'''
def box_elim(box_grouped, row):
    for test in box_grouped:
        print(test)
        boxs = test[1]
        row = test[0]
        found = False
        for box in boxs:
            for remove_value in row.needs:
                positions = box.cords_of_possibilities(remove_value)
                condtions_met = True
                for element in positions:
                    condtions_met = True
                    if row:
                        row_x = row.parts[0].x
                        print('Row_x is', row_x, 'element is', element)
                        if element[0] != row_x:
                            break

                    else:
                        col_x = row.parts[0].x
                        if positions[0][0] != element[0] and positions[0][0] == row_x:
                            condtions_met = False
                            break
                        else:
                            condtions_met = True                        

            if condtions_met:
                if row:
                    for cell in row.parts:
                        if cell.y != box.parts[0].y and cell.y != box.parts[3].y  and cell.y != box.parts[6].y:
                            cell.remove_pos(remove_value)
                            found = True
                            print("found")
                    if found:
                        return found
'''


def all_equal(check_list, value_to_check):
    for value in check_list:
        if value != value_to_check:
            return False
    return True


def pointing_pairs(line_box_group, row):

    for grouping in line_box_group:
        row = grouping[0]
        boxes = grouping[1]

        for box in boxes:
            for test_remove_value in row.needs:
                possible_locations = box.cords_of_possibilities(test_remove_value)

                if len(possible_locations) == 0:
                    continue
                if row:
                    possible_locations_x = []

                    for i in possible_locations:
                        possible_locations_x.append(i[0])

                    if not all_equal(possible_locations_x, row.parts[0].x):
                        break

                    if row:
                        for cell in row.parts:
                            if cell.y != box.parts[0].y and cell.y != box.parts[3].y and cell.y != box.parts[6].y:
                                cell.remove_pos(test_remove_value)



        


def show_board(board):
    disp_board = [[0 for col in range(9)] for row in range(9)]
    for i in range(9):
        for j in range(9):
            disp_board[i][j] = board[j][i].value
    print(*disp_board, sep='\n')


def main():
    board_img = grab_screen(abs2rel(383,380)+abs2rel(1132,1129))
    board_img_gray = cvtColor(board_img,COLOR_RGB2GRAY)
    board = [[Cell(0,0,0,0) for col in range(9)] for row in range(9)]
    for i in range(9):
        for j in range(9): 
            obj = board[i][j]
            obj.x = i
            obj.y = j


            if i <= 2 and j <= 2:
                box = 0
            elif 3 <= i <= 5 and j <= 2:
                box = 1
            elif 6 <= i and j <= 2:
                box = 2

            elif i <= 2 and 3 <= j <= 5:
                box = 3
            elif 3 <= i <= 5 and 3 <= j <= 5:
                box = 4
            elif i >= 6 and 3 <= j <= 5:
                box = 5

            elif i <= 2 and j >= 6:
                box = 6
            elif 3 <= i <= 5 and j >= 6:
                box = 7
            elif i >= 6 and j >= 6:
                box = 8

            obj.box = box


    while False:
        match_templat(board_img_gray,three_w,0.85,True)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break



    board = set_up_board(board , match_templat(board_img_gray,one_w,0.85) , 1)
    board = set_up_board(board , match_templat(board_img_gray,two_w,0.85) , 2)
    board = set_up_board(board , match_templat(board_img_gray,three_w,0.9) , 3)
    board = set_up_board(board , match_templat(board_img_gray,four_w,0.9) , 4)
    board = set_up_board(board , match_templat(board_img_gray,five_w,0.9) , 5)
    board = set_up_board(board , match_templat(board_img_gray,six_w,0.9,) , 6)
    board = set_up_board(board , match_templat(board_img_gray,seven_w,0.9) , 7)
    board = set_up_board(board , match_templat(board_img_gray,eight_w,0.9) , 8)
    board = set_up_board(board , match_templat(board_img_gray,nine_w,0.85) , 9)

    show_board(board)

    # Set up the same box and line since it cannot be done when intilised
    all_box = []
    all_col = []
    all_row = []

    for i in board:
        counter = 0
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
            
            if counter % 3 == 0:
                all_box.append(BHV(same_box))
                all_col.append(BHV(same_v_line))
            all_row.append(BHV(same_h_line))
            counter += 1
            
    # group boxes and rows toghet to better find pairs that can elemi pos
    good_box = [] 
    good_col = []
    good_row = all_row[0:9]
    for i in [0,9,18,1,10,19,2,11,20]:
        good_box.append(all_box[i])

    for i in range(0,27,3):
        good_col.append(all_col[i])

    col_box_group = []
    box_set_1 = [good_box[0],good_box[3],good_box[6]]
    box_set_2 = [good_box[1],good_box[4],good_box[7]]
    box_set_3 = [good_box[3],good_box[5],good_box[8]]

    row_box_group = []
    offset = 0
    loop = 1
    for row in good_row:
        box_set = []
        for i in range(3):
            box_set.append(good_box[i+offset])
        if loop % 3 == 0:
            offset += 3
        row_box_group.append([row,box_set])
        loop += 1

    for i in range(0,3):
        col_box_group.append([good_col[i],box_set_1])

    for i in range(3,6):
        col_box_group.append([good_col[i],box_set_2])

    for i in range(6,9):
        col_box_group.append([good_col[i],box_set_3])


    for i in range(30): 
        trim_all(board)    

    no_change = 0
    for x in range(200):

        before_board = [[0 for col in range(9)] for row in range(9)]
        for i in range(9):
            for j in range(9):
                before_board[i][j] = copy.deepcopy(board[i][j])
                pass

        for i in range(2): 
            trim_all(board)
            pass
        for i in all_row:
            i.last_one()
            pass
        for i in all_box:
            i.last_one()
            pass
        for i in all_col:
            i.last_one()
            pass
        
        
        if x > 10:
            for i in col_box_group:
                genral_pair(i[0],i[1],'col')
                pass
                
        if x > 10:
            for i in row_box_group:
                genral_pair(i[0],i[1],'row')
                pass
                
        if x > 15:
            trip_pair(good_box)
            trip_pair(good_col)
            trip_pair(good_row)
            pass

        if x > 18:
            pointing_pairs(row_box_group, True)
            pass

        
        for i in range(9):
            for j in range(9):
                if len(before_board[i][j].possibilities) != len(board[i][j].possibilities):
                    print('Before',before_board[i][j].possibilities, 'After',board[i][j].possibilities,f'({i},{j})') 
                    no_change = 0
                else:
                    no_change += 1
        
        if no_change >= 810:
            break
                        
        total = 0
        for i in board:
            for j in i:
                total += j.value
        if total == 405:
            print('Correct')
            break

    if True:
        input_board(board)

    if True:
        show_possibilities(board)

   
    show_board(board)
    x = 1
    y = 7
    print(f'({x},{y})', board[x][y].possibilities)
    x = 3
    y = 1
    print(f'({x},{y})', board[x][y].possibilities)

if __name__ == '__main__':
    time.sleep(3)
    main()