from numpy import round, delete, array
from classes import Cell
def set_up_board(board, new,value):
	y = round(new[0]/84)
	x = round(new[1]/84)
	prelim =[]
	#scufed solution just run it a bunch of times can add acutall logic later
	# deleats all duplicats found with matching
	for i in range(100):
		for i in range(len(x)):
			if i+2 <= len(x):
				if x[i] == x[i+1] and y[i] == y[i+1]:
					x = delete(x , i)
					y = delete(y , i)

	for i in range(len(x)):

		if x[i]<=2 and y[i]<=2:
			box = 0
		elif 3<=x[i]<=5 and y[i]<=2:
			box = 1
		elif 6<=x[i] and y[i]<=2:
			box = 2

		elif x[i]<=2 and 3<=y[i]<=5:
			box = 3
		elif 3<=x[i]<=5 and 3<=y[i]<=5:
			box = 4
		elif x[i]>=6 and 3<=y[i]<=5:
			box = 5

		elif x[i]<=2 and y[i]>=6:
			box = 6
		elif 3<=x[i]<=5 and y[i]>=6:
			box = 7
		elif x[i]>=6 and y[i]>=6:
			box = 8

		obj = Cell(value , int(x[i]) , int(y[i]), box)
		obj.possibilities = array([])
		board[int(x[i])][int(y[i])] = obj 

	return board