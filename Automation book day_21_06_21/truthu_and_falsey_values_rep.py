name = ''
while not name:
    name = input('Please enter your name:')
    print('How many guests will you have?')
    guest = int(input())
    if guest:
        print('Check, if you have enough space for the guests.')
    else:
        print('Prepare the rooms for the next day.')
print('Done!')