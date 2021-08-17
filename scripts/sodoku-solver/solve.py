import random
import numpy as np
import time
class sodoku:
    def __init__(self,grid,boxRange):
        self.grid = grid
        self.boxRange = boxRange
    def show(self):
        for row in self.grid:
            print(row)
    def solve(self):
        def possible(num,x,y):
            def box(x,y):                       
                board = np.array(self.grid)
                result = {}
                size = 3
                for i in range(len(board) // size):
                    for j in range(len(board) // size):
                        values = board[j * size:(j + 1) * size, i * size:(i + 1) * size]
                        result[i * size + j + 1] = values.flatten()
                if y <= 2 and x <= 2:
                    squareBox = result[1]
                if (y <= 5 and y > 2) and x <= 2:
                    squareBox = result[2]
                if (y <= 8 and y > 5) and x <= 2:
                    squareBox = result[3]

                if (y <= 2 ) and (x <= 5 and x > 2):
                    squareBox = result[4]
                if (y <= 5 and y > 2)and (x <= 5 and x > 2):
                    squareBox = result[5]
                if (y <= 8 and y > 5)and (x <= 5 and x > 2):
                    squareBox = result[6]
            
                if (y <= 2) and (x <= 8 and x > 5):
                    squareBox = result[7]
                if (y <= 5 and y > 2)and (x <= 8 and x > 5):
                    squareBox = result[8]
                if (y <= 8 and y > 5)and (x <= 8 and x > 5):
                    squareBox = result[9]
                return squareBox
            row = self.grid[y]
            column= [r[x] for r in self.grid]
            square = box(x,y)
            if (num not in row) and (num not in column) and (num not in square):
                return True
            else:
                return False
        y = 0
        for row in self.grid:
            x = 0
            for number in row:
                if number == 0:
                    indexes.append(indexCount)
                    for i in range(1,10):
                        
                x += 1
            y += 1


           
boxRange = "3x3"           
bxd = []
with open('board.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(' ')
        bLine = [int(x) for x in line]
        bxd.append(bLine)
# brd = [[3,0,0,2],[0,4,1,0],[0,3,2,0],[4,0,0,1]]
brd = sodoku(bxd,boxRange)
brd.show()
brd.solve()
print('-----Solved------')
brd.show()