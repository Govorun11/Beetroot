'''
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10,

and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
'''

import random

first_list = []
second_list = []
i = 0
while i <= 19:
    if i < 10:
        fl = random.randint(0, 10)
        first_list.append(fl)
    elif i >= 10:
        sl = random.randint(0,10)
        second_list.append(sl)
    i += 1
print(f'First list: {first_list}!')
print(f'Second list: {second_list}!')
firstANDsecond = first_list + second_list
common_set = set(firstANDsecond)
print(f'Common list: {common_set}')