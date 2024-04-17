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
			'''
		if self.x == 1 and self.y == 5:
			for i in range(9):
				print(self.box_mates[i].value, end='')
			print(' ')
'''

	def check_sys(self, mates, needed):
		

		for need in needed:
			can = []
			for obj in mates:
				for pos in obj.possibilities:
					if pos == need:
						can.append([obj,need])
			if len(can) == 1:
				can[0][0].value = can[0][1]
				can[0][0].possibilities = []
				return True
				#print(can[0][0].value, can[0][1])

		return False




'''

		candidates = []
		for obj in self.box_mates:
			for pos in obj.possibilities:
				for need in self.needed_b:
					candidates = []
					if pos == need:
						candidates.append([obj,need])
							#print('appended',obj.possibilities,need )
				if len(candidates) == 1:
					candidates[0][0].value = candidates[0][1]
					print(candidates[0][0].value, 'and' , candidates[0][1])
					break

'''

'''
class Row():
	def __init__(self, Tiles):
		self.needed = np.array([1,2,3,4,5,6,7,8,9])
		self.Tiles = Tiles

	def trim_row(self):
		for i in Tiles:
			self.needed = np.delete(self.needed ,np.where(self.needed == i.value))
'''


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

	def pairs(self,box):
		if len(needs)==2:
			pass
		