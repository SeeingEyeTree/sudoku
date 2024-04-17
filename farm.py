
from main import main
from pyautogui import click
from time import sleep


def farm(n):
    for _ in range(n):
        main()
        sleep(4)
        click(1357,1011)
        sleep(0.1)
        click(1357,910)
        sleep(5)


farm(10)