import cv2
from cv2 import cvtColor,imread,COLOR_RGB2GRAY, TM_CCOEFF_NORMED
import time
import numpy as np
import pyautogui
from grab_screen import grab_screen
from rel_cords import abs2rel
from keys import WASD
from match_templat import match_templat
from set_up_board import set_up_board
#website used on a chrome browser with book mark bar on https://sudoku.com

debug = False # I know there is a module just don't feel like learing it right now 

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

#one_w=cv2.imread("C:/Users/malco/OneDrive/Documents/GitHub/sudoku/images/one_w.png")

#bounds for a 2560 * 1600 screen top (383,380) bot (1132,1129)
#one cell is ~83.2222222222 84 pixles tall and wide 84*84
time.sleep(4)

board_img = grab_screen(abs2rel(383,380)+abs2rel(1132,1129))
board_img_gray = cvtColor(board_img,COLOR_RGB2GRAY)



while True:
	cv2.imshow('window',board_img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

#read values into array from img

thres = 0.9

board = np.zeros((9,9))
#print(board)

test = match_templat(board_img_gray,one_w,thres)


board = set_up_board(board , match_templat(board_img_gray,one_w,thres) , 1)
board = set_up_board(board , match_templat(board_img_gray,two_w,thres) , 2)
board = set_up_board(board , match_templat(board_img_gray,three_w,thres) , 3)
board = set_up_board(board , match_templat(board_img_gray,four_w,thres) , 4)
board = set_up_board(board , match_templat(board_img_gray,five_w,thres) , 5)
board = set_up_board(board , match_templat(board_img_gray,six_w,thres) , 6)
board = set_up_board(board , match_templat(board_img_gray,seven_w,thres) , 7)
board = set_up_board(board , match_templat(board_img_gray,eight_w,thres) , 8)
board = set_up_board(board , match_templat(board_img_gray,nine_w,thres) , 9)

print(board)

'''
while True:
	y1,x1=match_templat(board_img_gray,one_w,0.9)
	print(np.round(x1/84))
	print(np.round(y1/84))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
'''




