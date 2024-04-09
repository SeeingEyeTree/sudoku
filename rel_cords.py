from pyautogui import size
from math import floor

def abs2rel(x,y):
	return floor(x/2560*size()[0]), floor(y/1600*size()[1])



if __name__ == "__main__":
	print(abs2rel(500,1000))