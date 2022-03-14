import random
myNumber = random.randint(1,20)
print('I\'m thinking of the number from th range 1-20.')
print('You have 6 tries. Try to guess my number.')
for guess_try in range(1,7):
    guess = int(input('Enter the the number: '))

    if guess < myNumber:
        print('Your number is too low.')
    elif guess > myNumber:
        print('Your number is too high.')
    else:
        break
if guess == myNumber:
    print(f'Excellent job!. You guessed my number in {guess_try} try.')
else:
    print(f'Nope. The number I was thinking of was {str(myNumber)}')

