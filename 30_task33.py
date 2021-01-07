'''
TASK 3

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter

(to keep things simple let it only be ‘+’, ‘-’ or ‘*’)

and an arbitrary number of arguments (only numbers) as the second parameter.

Then return the sum or product of all the numbers in the arbitrary parameter. For example:

'''
def make_operation (operation, *args):
    for number in args:
        d = 1
        s = 0
        if operation == '+':
            s += number
            return s
        elif operation == '-':
            s -= number
            return s
        else:
            d *= number
        return d
print(make_operation('*', 7, 6))