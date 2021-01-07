'''
TASK 1

Make a program that has some sentence (a string) on input

and returns a dict containing all unique words as keys and the number of occurrences as values.
'''
import string

my_string = input('Input anything sentence: ').lower()

for delim in string.punctuation:
    my_string = my_string.replace(delim, ' ')

my_string = my_string.split(' ')
my_dict = {}
for word in set(my_string):
    my_dict[word] = my_string.count(word)
print(my_dict)

'''
Task 2
Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock
'''

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_items = {}
total_price = 0
for key, value in stock.items() and prices.items():
    total_items[key] = prices.get(key, 0) * stock.get(key, 0)
    total_price += total_items[key]
print(f'Total price for every key of stock: {total_items}')
print(f'Total price of stock: {total_price}.')

'''
Task 3

List comprehension exercise

Use a list comprehension to make a list
containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
'''


my_list = [(i, i**2) for i in range(1,11)]
print(my_list)
