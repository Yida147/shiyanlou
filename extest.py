#!/usr/bin/env pyhton3

num = input('Enter number:')
for n in num:
    if type(n) != int:
        raise TypeError() 
try:
    new_num = int(num)
    print('INT:{}'.format(new_num))
except:
    print('Error: abc')

