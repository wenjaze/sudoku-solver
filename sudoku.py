#!/usr/bin/env python3
''' 
S U D O K U  SOLVER
Author: Gergely Raska 
Created: 2020.05.18

'''

from array import *

# implementation of board class
# funtions:solve,getempty,print,(printboxvalues)
class Board(object):
	
	def __init__(self,values):
		self.values = values
		self.bd = 3 # box divider constant
		self.dim = 9 # matrix constant dimension  (if board dim != 9x9 : len(self.values[0]))

	# backend
	
	#not callable outside the class
	def GetNextEmpty(self,board):
		b = []
		for r in range(self.dim):
			for c in range(self.dim):
				if self.values[r][c] == 0:
					b.append(r//self.bd)
					b.append(c//self.bd)
					return r,c,b

				if r == self.dim -1 and c == self.dim -1:
					print("returning NONE -----------------------------------------------")
					return None

	def Solve(self):
		print("lefut")
		found = self.GetNextEmpty(self.values)
		if found:
			print("ROW : "+str(found[0])+"\nCOL :"+str(found[1])+"\nBOX : "+str(found[2][0])+","+str(found[2][1]))
			for number in range(1,10):
				if self.FindCorrectNumber(found,number):

					self.values[found[0]][found[1]] = number
					print("inserting number"+str(number)+" to : ("+str(found[0])+","+str(found[1])+")")
					self.Print()
					if self.Solve():
						return True
					
					
					self.values[found[0]][found[1]] = 0
		else:
			return True

		return False

	def FindCorrectNumber(self,v,number):
		print("finding...")
		r = v[0]
		print("row = "+str(r))
		c = v[1]
		print("col = "+str(c))
		b = v[2]
		print("box = ["+str(b[0])+","+str(b[1])+"]")

		# checking box
		print("trying "+str(number)+" to : ("+str(r)+","+str(c)+")")
		for br in range(b[0]*3,b[0]*3+self.bd):
			for bc in range(b[1]*3,b[1]*3+self.bd):
				if self.values[br][bc] == number and [br,bc] != [r,c]:
					print("duplicate of "+str(number)+" at box : ("+str(b[0])+","+str(b[1])+")")

					return False
		# check col			
		for row in range(self.dim):
			for col in range(self.dim):
				if self.values[row][c] == number and row != r:
					print("duplicate of "+str(number)+" at row : ("+str(row)+")")
					return False
		# check row
		for row in range(self.dim):
			for col in range(self.dim):
				if self.values[r][col] == number and col != c:
					print("duplicate of "+str(number)+" at col : ("+str(col)+")")
					return False
		return True
	# frontend
	def Print(self):
		print("BOARD:\n")
		for r in self.values:
			for c in r:
				print(c,end=" ")
			print()

	def PrintBoxIndices(self):
		for r in range(self.dim):
			for c in range(self.dim):
				#print(c,end=" ")
				print("("+str(int(r/self.bd))+","+str(int(c/self.bd))+")",end=" ")
			print()
			print()

def main():

	board_values = [
		[0, 0, 0, 8, 7, 1, 0, 0, 0],
        [0, 4, 9, 0, 0, 0, 1, 0, 5],
        [2, 0, 8, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 7, 0, 6, 0, 0, 0],
        [1, 7, 0, 0, 2, 0, 0, 9, 4],
        [0, 0, 0, 9, 0, 3, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 9, 0, 7],
        [8, 0, 4, 0, 0, 0, 3, 6, 0],
        [0, 0, 0, 1, 6, 4, 0, 0, 0]
		]

	myBoard = Board(board_values)
	myBoard.Solve()
	myBoard.Print()

	
if __name__ == '__main__':
	main()

