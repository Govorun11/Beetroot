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

while len(first_list) < 10:
    first_list.append(random.randint(0, 10))
    second_list.append(random.randint(0, 10))

print(f'First list: {first_list}!')
print(f'Second list: {second_list}!')
first_and_second = first_list + second_list
print(f'First and second lists: {first_and_second}!')
common_set = set(first_and_second)
print(f'Common list: {list(common_set)}')
