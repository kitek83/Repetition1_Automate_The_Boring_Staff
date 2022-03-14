name = ''
while not name:
    print('Enter Your name: ')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Make sure, you have enough space.')
print('Done!')
