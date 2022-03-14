plyer_inv = {'rope':1, 'torch':6, 'goldCoin': 42, 'dagger':1, 'arrow':12}

def inventory(invent):
    print('Inventory: ')
    totalInv = 0
    for k,v in invent.items():
        totalInv += v
        print(k,':',v)
    print('Total inventory is ' + str(totalInv))


inventory(plyer_inv)
