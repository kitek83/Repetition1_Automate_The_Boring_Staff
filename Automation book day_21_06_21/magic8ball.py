import random
messages = ['hello world',
            'how are you',
            'you are the king',
            'you are completely right',
            'we will see',
            'let\'s do it']
print(messages[random.randint(0,len(messages) +1)])
name ='Krzysztof'
for i in name:
    print('*******' + i + '******')
print(id('Kris'))