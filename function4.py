def spam():
    eggs = 'spam local'
    print(eggs) #print spam local
def bacon():
    eggs = 'bacon local'
    print(eggs) #print bacon local
    spam()
    
global eggs
eggs = 'global'

bacon()
print(eggs)