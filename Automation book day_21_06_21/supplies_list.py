supplies = ['pens', 'staplers', 'flamethrowers', 'blinders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' from the supplies list is ' + supplies[i])
print('-------------------------')
print()
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' from the supplies list is: ' + item)
