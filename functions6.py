def spam(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print('Error: invalid argument')

print(spam(2))
print(spam((42)))
print(spam(4))
print(spam(0))