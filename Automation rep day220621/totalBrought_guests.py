allGuests = {'Kris':{'cakes':15,'cola':4, 'apples':3},
             'Bob':{'apples': 5, 'pretzels': 12, 'cola':6},
             'Alice':{'cakes':10, 'pretzels':7, 'cups':10}}

def totalBrought(guests,item):
   numberBrought = 0
   for k,v in guests.items():
       numberBrought += v.get(item,0)
   return  numberBrought

print('Quantity of total brought products.')
print('Cakes: ' + str(totalBrought(allGuests,'cakes')))
print('Cola: ' + str(totalBrought(allGuests,'cola')))
print('Apples: ' + str(totalBrought(allGuests,'apples')))
print('Pretzels: ' + str(totalBrought(allGuests,'pretzels')))
print('Cups: ' + str(totalBrought(allGuests,'cups')))