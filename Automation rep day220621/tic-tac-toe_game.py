theBoard = {'top-L':'','top-M':'','top-R':'',
            'mid-L':'','mid-M':'','mid-R':'',
            'low-L':'','low-M':'','low-R':''}
def board(board):
    print(board['top-L']+' |' + board['top-M'] + ' |' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])

turn = 'x'
for i in range(9):
    board(theBoard)
    print('Now it is turn of ' + turn + '.Enter your move: ')
    move = input()
    theBoard[move] = turn
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'


board(theBoard)