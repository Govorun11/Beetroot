'''
TASK1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
'''
import  random

my_list = []
i = 0
while i <= 10:
    x = random.randint(0, 10)
    my_list.append(x)
    i+=1
else:
    print(f'Our list is {my_list}!')
    print(f'Largest number of  list is {max(my_list)}!')



'''
TASK2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10,

and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers

'''
import random

first_list = []
second_list = []

while len(first_list) < 10 and len(second_list) < 10:
        first_list.append(random.randint(0,10))
        second_list.append(random.randint(0,10))

print(f'First list: {first_list}!')
print(f'Second list: {second_list}!')
first_and_second = first_list + second_list
print(f'First and second lists: {first_and_second}!')
common_set = set(first_and_second)
print(f'Common list: {list(common_set)}')

'''
TASK 3
Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration
'''

divisible_list = []
for i in range(0, 100):
    if i % 7 == 0 and i % 5 != 0:
        divisible_list.append(i)
        i += 1
print(divisible_list)
