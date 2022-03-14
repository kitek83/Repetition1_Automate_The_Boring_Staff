import random
def getAnswer(ans_n):
    if ans_n == 1:
        print('Ypu are right.')
    elif ans_n == 2:
        print('It is decidely so.')
    elif ans_n == 3:
        print('Yes')
    elif ans_n == 4:
        print('reply hazy and try again')
    elif ans_n == 5:
        print('Ask again later.')

r = random.randint(1,5)
getAnswer(r)
