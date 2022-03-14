import random
WIDTH = 60
HEIGHT = 20
nextCells = []
count =0
for x in range(WIDTH):
    count += 1
    columns = []
    for y in range (HEIGHT):

        if random.randint(0,1) == 0:
            columns.append('#')
        else:
            columns.append(' ')

    nextCells.append(columns)
    print(count)
    print(nextCells)

