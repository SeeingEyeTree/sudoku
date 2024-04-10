import cv2
from cv2 import cvtColor,imread,COLOR_RGB2GRAY, TM_CCOEFF_NORMED
import time
import numpy as np
import pyautogui
from grab_screen import grab_screen
from rel_cords import abs2rel
from keys import WASD, PR, ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE
from match_templat import match_templat
from set_up_board import set_up_board
from classes import Tile
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
#time.sleep(1)

board_img = grab_screen(abs2rel(383,380)+abs2rel(1132,1129))
board_img_gray = cvtColor(board_img,COLOR_RGB2GRAY)


if debug:
	while True:
		cv2.imshow('window',board_img)
		if cv2.waitKey(25) & 0xFF == ord('q'):
	            cv2.destroyAllWindows()
	            break

#read values into array from img

thres = 0.81

board = [[Tile(0,0,0,0) for col in range(9)] for row in range(9)]

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

if True:
	while True:
		match_templat(board_img_gray,six_w,0.9,True)
		if cv2.waitKey(25) & 0xFF == ord('q'):
	            cv2.destroyAllWindows()
	            break

board = set_up_board(board , match_templat(board_img_gray,one_w,0.85) , 1)
board = set_up_board(board , match_templat(board_img_gray,two_w,0.9) , 2)
board = set_up_board(board , match_templat(board_img_gray,three_w,0.9) , 3)
board = set_up_board(board , match_templat(board_img_gray,four_w,0.9) , 4)
board = set_up_board(board , match_templat(board_img_gray,five_w,0.9) , 5)
board = set_up_board(board , match_templat(board_img_gray,six_w,0.9,) , 6)
board = set_up_board(board , match_templat(board_img_gray,seven_w,0.9) , 7)
board = set_up_board(board , match_templat(board_img_gray,eight_w,0.9) , 8)
board = set_up_board(board , match_templat(board_img_gray,nine_w,0.9) , 9)

time.sleep(4)

for i in range(300):
	for i in board:
		for obj in i:
			if obj.value == 0:
				same_box = []
				same_h_line = []
				same_v_line = []

				for comp_i in board:
					for comp_obj in comp_i:
						# might be able to put everything under the same umbrel but nice to seprate out might be useful later
						# will catch itself but since value is 0 does not matter
						if obj.box == comp_obj.box:
							same_box.append(comp_obj)

						if obj.x == comp_obj.x:
							same_h_line.append(comp_obj)

						if obj.y == comp_obj.y:
							same_v_line.append(comp_obj)


				obj.trim(same_box , same_h_line, same_v_line)
				if obj.x == 1 and obj.y == 8:
					for i in same_box:
						#print(i.value)
						pass


for i in board:
	for j in i:
		if j.value == 1:
			PR(ONE)
		elif j.value == 2:
			PR(TWO)
		elif j.value == 3:
			PR(THREE)
		elif j.value == 4:
			PR(FOUR)
		elif j.value == 5:
			PR(FIVE)
		elif j.value == 6:
			PR(SIX)
		elif j.value == 7:
			PR(SEVEN)
		elif j.value ==8:
			PR(EIGHT)
		elif j.value ==9:
			PR(NINE)

		WASD('D',0.05)
	for i in range(9):
		WASD("U")

	WASD("R")


