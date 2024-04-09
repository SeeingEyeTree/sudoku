import cv2
from cv2 import cvtColor,imread,COLOR_RGB2GRAY, TM_CCOEFF_NORMED
import time
import numpy as np
import pyautogui
from grab_screen import grab_screen
from rel_cords import abs2rel
from keys import WASD

#website used on a chrome browser with book mark bar on https://sudoku.com


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
"""
while True:
	cv2.imshow('window',board_img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
"""

#read values into array from img


def match_templat(where,what,threshold,test=False):
    res = cv2.matchTemplate(where,what,TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    if test:
	    whereRGB=cv2.cvtColor(where,cv2.COLOR_GRAY2RGB)
	    w1, h1 = what.shape[::-1]
	    for pt1 in zip(*loc[::-1]):
	            cv2.rectangle(whereRGB, pt1, (pt1[0] + w1, pt1[1] + h1), (0,0,255), 2)
	    cv2.imshow('matches',whereRGB)
	    print(loc)
    y=loc[1]
    x=loc[0]
    return x,y


thres = 0.9

y1,x1 = match_templat(board_img_gray,one_w,thres)
'''
y2,x2 = match_templat(board_img_gray,two_w,thres)
y3,x3 = match_templat(board_img_gray,three_w,thres)
y4,x4 = match_templat(board_img_gray,four_w,thres)
y5,x5 = match_templat(board_img_gray,five_w,thres)
y6,x6 = match_templat(board_img_gray,six_w,thres)
y7,x7 = match_templat(board_img_gray,seven_w,thres)
y8,x8 = match_templat(board_img_gray,eight_w,thres)
y9,x9 = match_templat(board_img_gray,nine_w,thres)
'''


while True:
	y1,x1=match_templat(board_img_gray,one_w,0.9,True)
	print(np.round(x1/84))
	print(np.round(y1/84))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break





