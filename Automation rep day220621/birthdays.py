birthdays = {'Alise':'Apr 1', 'Bob':'May 12', 'Kris': 'June 6','Alan':'Feb 12'}
while True:
    print('Enter the searches name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] +' is the birthdays date of the ' + name + ".")
    else:
        print('Name was not found.')
        b_data = input('Enter birthday date: ')
        birthdays[name] = b_data
        print('Dictionary was updated.')
        print('birthdays=',birthdays)

print('###################################')
for v in birthdays.values():
    print(v)
print('========================')
for k in birthdays.keys():
    print(k)
print('---------------------------')
for item in birthdays.items():
    print(item)