import random
def coltaz(number):
    if number % 2 == 0:
        print(number//2)
    else:
        print(3*number + 1)
for x in range(101):
    n = random.randint(1,101)
    coltaz(n)