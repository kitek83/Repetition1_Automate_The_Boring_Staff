#! python3
#bulletPointAdder.py - Ads Wikipedia bullet points to the start
#of each line of the text on the clipboard
import pyperclip

text = pyperclip.paste()
print(text)
#now we want to split the text
lines = text.split('\n')

print(lines)
print(len(lines))
#adding the * on the beggining of each line
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
print(lines)
text = '\n'.join(lines)
print(text)
pyperclip.copy(text)