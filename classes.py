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
		self.box_mates = []
		self.h_line_mates = []
		self.v_line_mates = []

	def trim(self, box, h_line, v_line):
		self.box_mates = box
		self.h_line_mates = h_line
		self.v_line_mates = v_line

		#I know it does not need to be reacluated every time but will fix later what class is for

		if len(self.possibilities)>1:
			for i in box:
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


	def check_sys(self, mates, needed):
		candidates = []
		for need in needed:
			for obj in mates:
				for pos in obj.possibilities:
					if pos == need:
						candidates.append([obj,need])
						#print('append', obj.possibilities,need)

			if len(candidates) == 1 and candidates[0][0].value == 0:
				candidates[0][0].value = candidates[0][1]
				candidates[0][0].possibilities = np.array([])
				#print('replace(', candidates[0][0].x,candidates[0][0].y,')', candidates[0][1])







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


