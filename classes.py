import numpy as np


class Tile():
	
	def __init__(self, value,x,y,box):
		self.value = value
		self.x = x
		self.y = y
		self.box = box
		self.possibilities = np.array([1,2,3,4,5,6,7,8,9])
		self.box_mates = []

	def trim(self, box, h_line, v_line):
		self.box_mates = box
		if len(self.possibilities)>1:
			for i in box:
				self.possibilities = np.delete(self.possibilities , np.where(self.possibilities == i.value)[0])

			for i in h_line:
				self.possibilities = np.delete(self.possibilities , np.where(self.possibilities == i.value)[0])

			for i in v_line:
				self.possibilities = np.delete(self.possibilities , np.where(self.possibilities == i.value)[0])

		if len(self.possibilities) == 1:
			self.value =  self.possibilities[0]


class Row():
	def __init__(self, Tiles):
		self.needed = np.array([1,2,3,4,5,6,7,8,9])
		self.Tiles = Tiles

	def trim_row(self):
		for i in Tiles:
			self.needed = np.delete(self.needed ,np.where(self.needed == i.value))



