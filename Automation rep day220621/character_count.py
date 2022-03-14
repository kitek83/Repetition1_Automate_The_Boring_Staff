message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
spam = {}
for character in message:
    spam.setdefault(character,0)
    spam[character] = spam[character] + 1
print(spam)