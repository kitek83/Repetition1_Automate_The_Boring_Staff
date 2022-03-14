import copy

import cppy
def eggs(parameter):
    parameter.append('Hello')
    print(parameter)

list =[1,2,3,4]
eggs(list)
print('-----------------')
list1 = ['A','B','C','D','E']
print(id(list1))
copy_list = copy.copy(list1)
copy_list[1] = 34
print('list1=',list1)
print('copy_list=',copy_list)