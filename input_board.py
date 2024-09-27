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
                pass
            elif j.value == 2:
                PR(TWO)
                pass
            elif j.value == 3:
                PR(THREE)
            elif j.value == 4:
                PR(FOUR)
            elif j.value == 5:
                PR(FIVE)
            elif j.value == 6:
                #PR(SIX)
                pass
            elif j.value == 7:
                PR(SEVEN)
            elif j.value == 8:
                PR(EIGHT)
            elif j.value == 9:
                PR(NINE)
                pass

            WASD('D',0.002)
        for i in range(9):
            WASD("U",0.002)

        WASD("R",0.002) 

# not relative cords for this one
def show_possibilities(board):
    click(1480,420)
    not_solved = []

    for i in board:
        for j in i:
            if j.value == 0:
                not_solved.append(j)

    for i in not_solved:
        click(420+i.x*84,420+i.y*84)
        if True: #len(i.possibilities) <= 3:
            for j in i.possibilities:
                if j == 1:
                    PR(ONE)
                    pass
                elif j == 2:
                    PR(TWO)
                    pass
                elif j == 3:
                    PR(THREE)
                elif j == 4:
                    PR(FOUR)
                elif j == 5:
                    PR(FIVE)
                elif j == 6:
                    PR(SIX)
                    pass
                elif j == 7:
                    PR(SEVEN)
                elif j == 8:
                    PR(EIGHT)
                elif j == 9:
                    PR(NINE)
                    pass
                sleep(0.005)
    click(1480,420)