import random
rows = 3
columns = 4
list = [[0,0,0,0],
        [0,5,0,0],
        [0,0,0,0]]
#print(list[1][1])
list1 = []
for x in range(rows):
    list2 = []
    for y in range (columns):
        list[x][y] = random.randint(1,100)
        if random.randint(0,1) == 0:
            list2.append('#')
        else:
            list2.append(' ')
    list1.append(list2)
    print(list1)