'''
Write a Python program to detect the number of local variables declared in a function.
'''


def my_func():
    a, b = 1, 2
    my_list = [2, 1, 4, 6]
    my_string = 'lkflsjdng'
    d = {}


print(f'{my_func.__name__} has {my_func.__code__.co_nlocals} local variables!')
