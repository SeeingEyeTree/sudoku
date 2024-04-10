from numpy import round, delete



def set_up_board(board, new,value):
	x = round(new[0]/84)
	y = round(new[1]/84)
	#scufed solution just run it a bunch of times can add acutall logic later
	# deleats all duplicats found with matching
	for i in range(100):
		for i in range(len(x)):
			if i+2 <= len(x):
				if x[i] == x[i+1] and y[i] == y[i+1]:
					x = delete(x , i)
					y = delete(y , i)
	

	for i in range(len(x)):
		board[int(x[i]),int(y[i])] = value
	
	return board