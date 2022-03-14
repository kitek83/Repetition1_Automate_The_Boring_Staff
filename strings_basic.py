while True:
    print('Enter the name:')
    name = input()
    if name != 'Joe':
       continue
    print(f'Hello {name}. Enter the pssword:')
    password = input()
    if password == 'swordfish':
        break
print('Access granted!')