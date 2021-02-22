'''
Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
 "add called with 4, 5"

def logger(func):
    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
'''


def logger(func):
    def inner(*args, **kwargs):
        print(f'{func.__name__} called with {args}')
        func(*args, **kwargs)
    return inner


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(4, 5, 6, 7, 8, 9, 9)
