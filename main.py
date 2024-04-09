import cv2
import time
import pyautogui
from grab_screen import grab_screen
from rel_cords import abs2rel
from keys import WASD
#website used on a chrome browser with book mark bar on https://sudoku.com


#bounds for a 2560 * 1600 screen top (383,380) bot (1132,1129)
#one cell is ~83.2222222222 84 pixles tall and wide 84*84
time.sleep(4)

board_img = grab_screen(abs2rel(383,380)+abs2rel(1132,1129))
while True:
	cv2.imshow('window',board_img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
