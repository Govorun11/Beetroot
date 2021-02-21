# Task 2
# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def my_func(power):
    def new_func(*args):
        return sum((x ** power for x in args))

    return new_func


print(my_func(2)(2, 3, 4, 5))
