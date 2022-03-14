import copy
import random, time
WIDTH = 60
HEIGHT = 20

#create list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)
print(nextCells)