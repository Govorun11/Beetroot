'''
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