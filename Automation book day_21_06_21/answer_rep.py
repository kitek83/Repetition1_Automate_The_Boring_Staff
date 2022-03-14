import random
def main():

    r= random.randint(1,3)
    answer = get_answer(r)
    print(answer)



def get_answer(num):
    if num == 1:
        return 'Of course, yes!'
    elif num == 2:
        return 'You are completely right'
    elif num == 3:
        return 'Excellent, you are good'
main()