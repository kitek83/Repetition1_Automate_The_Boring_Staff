#this is game program: rock, paper, scissors
import random
import sys
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
while True:
    print('%s Wins, %s Losses, %s Ties'%(wins,losses,ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit:')
        plyerMOve = input()
        if plyerMOve == 'q':
            sys.exit() #quit from the game/ program
        if plyerMOve == 'r' or plyerMOve == 'p' or plyerMOve == 's':
            break #we jump out from the current loop

        # player moves
    if plyerMOve == 'r':
        print('Rock versus ...')
    elif plyerMOve == 'p':
        print('Paper versus...')
    elif plyerMOve == 's':
        print('Scissors versus...')

        # computer moves
    computerMove = random.randint(1, 3)
    if computerMove == 1:
        computerMove = 'r'
        print('Rock')
    elif computerMove == 2:
        computerMove = 'p'
        print('Paper')
    elif computerMove == 3:
        print('Scissors')

    if plyerMOve == computerMove:
        ties += 1
    #wins on the side of the plyer
    if plyerMOve == 'r' and computerMove == 's':
        wins += 1
    elif plyerMOve == 'p' and computerMove == 'r':
        wins += 1
    elif plyerMOve == 's' and computerMove == 'p':
        wins += 1
    #losses on the side of the plyer
    if plyerMOve == 'r' and computerMove == 'p':
        losses += 1
    elif plyerMOve == 'p' and computerMove == 's':
        losses += 1
    elif plyerMOve == 's' and computerMove == 'r':
        losses += 1






























