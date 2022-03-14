items = {'cola':3, 'pizza':2}
print('I took ' + str(items.get('cola',0)) + ' bottles of cola and ' + str(items.get('pizza',0)) + ' pizza for picnic.')

dict1 = {'food':'pizza', 'age':5}
dict1.setdefault('color','black')
print(dict1)
dict1.setdefault('color','white')
print(dict1)