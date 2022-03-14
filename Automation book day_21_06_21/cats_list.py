cats = []
while True:
    print('Enter the name of the cat' + str(len(cats) + 1) +
          ' or write nothing to quit the program:')
    cat = input()
    cats += [cat]
    if cat == '':
        break
    for cat_name in cats:
        print(' ' + cat_name)