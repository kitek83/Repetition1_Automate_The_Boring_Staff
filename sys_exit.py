import sys
while True:
    print('Type exit to exit the program:')
    respond = input()
    if respond == 'exit':
        #break
        sys.exit()
    print('You typed ' + respond + '.')
print('Goodbye!')