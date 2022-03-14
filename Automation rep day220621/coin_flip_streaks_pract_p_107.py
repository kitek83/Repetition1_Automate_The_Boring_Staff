import random
numberOfStreaks = 0
list = []
for fli_coin in range(10000):
    if random.randint(0,1) == 0:
        list.append('H')
    else:
        list.append('T')
print(list)
