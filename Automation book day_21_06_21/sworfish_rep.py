while True:
    print('Enter Your name:')
    name = input()
    if name != 'Joe':
        continue #in this moment program jumps back to name - input()
    print('Hello Joe. Try to guess the pssword: ')
    password = input()
    if password == 'swordfish':
        print('Excellent job. Thi is right password.')
        break
    else:
        print('Password is wrong. Try again.')