'''
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10,

and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
SECOND VARIANT=)
'''
import random

first_list = []
second_list = []
i = 0
while len(first_list) < 10 and len(second_list) < 10:
        fl = random.randint(0, 10)
        sl = random.randint(0,10)
        first_list.append(fl)
        second_list.append(sl)
i += 1
print(f'First list: {first_list}!')
print(f'Second list: {second_list}!')
first_and_second = first_list + second_list
print(f'First and second lists: {first_and_second}!')
common_set = set(first_and_second)
print(f'Common list: {common_set}')