from pyautogui import click
from keys import WASD, PR, ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE
from time import sleep
def input_board(board):
    click(420,420)
    sleep(0.1)
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
            elif j.value == 8:
                PR(EIGHT)
            elif j.value == 9:
                PR(NINE)

            WASD('D',0.002)
        for i in range(9):
            WASD("U",0.002)

        WASD("R",0.002) 