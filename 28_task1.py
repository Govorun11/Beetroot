'''
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