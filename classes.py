import numpy as np


class Cell():

	def __init__(self, value,x,y,box):
		self.value = value
		self.x = x
		self.y = y
		self.box = box
		self.possibilities = np.array([1,2,3,4,5,6,7,8,9])
		self.needed_h = np.array([1,2,3,4,5,6,7,8,9])
		self.needed_v = np.array([1,2,3,4,5,6,7,8,9])
		self.needed_b = np.array([1,2,3,4,5,6,7,8,9])
		self.h_line_mates = []
		self.v_line_mates = []
		self.box_mates = []

	def trim(self, box, h_line, v_line):
		self.box_mates = box
		self.h_line_mates = h_line
		self.v_line_mates = v_line
		#I know it does not need to be reacluated every time but will fix later what class is for

		if len(self.possibilities)>1:
			for i in self.box_mates:
				self.possibilities = np.delete(self.possibilities , np.where(self.possibilities == i.value)[0])
				self.needed_b = np.delete(self.needed_b , np.where(self.needed_b == i.value)[0])


			for i in h_line:
				self.possibilities = np.delete(self.possibilities , np.where(self.possibilities == i.value)[0])
				self.needed_h = np.delete(self.needed_h , np.where(self.needed_h == i.value)[0])


			for i in v_line:
				self.possibilities = np.delete(self.possibilities , np.where(self.possibilities == i.value)[0])
				self.needed_v = np.delete(self.needed_v , np.where(self.needed_v == i.value)[0])


		if len(self.possibilities) == 1:
			self.value =  self.possibilities[0]
			self.possibilities = np.array([])


class BHV():
	def __init__(self,parts):
		self.parts = parts
		#self.name = name
		self.needs = np.array([1,2,3,4,5,6,7,8,9])

	def last_one(self):
		for i in self.parts:
			self.needs = np.delete(self.needs, np.where(self.needs == i.value)[0])

		for need in self.needs:
			can = []
			for obj in self.parts:
				for pos in obj.possibilities:
					if pos == need:
						can.append([obj,need])
			if len(can) == 1:
				can[0][0].value = can[0][1]
				can[0][0].possibilities = []


	def pairs(self,row,box):
		#print(row.needs,box.needs,box.parts[0].box)
		if len(row.needs) == 2 and len(box.needs) == 3:
			row_empty = []
			box_empty = []
			for i in row.parts:
				if i.value == 0:
					row_empty.append(i)

			for i in box.parts:
				if i.value == 0:
					box_empty.append(i)

			if row_empty[0].box == row_empty[1].box:
				# all condtions good
				# remove the row cells from the box empty
				box_empty = np.delete(box_empty, np.where(box_empty == row_empty)[0])
				print(box_empty)

	def show(self):
		for i in self.parts:
			print(i.value)
