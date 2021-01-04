'''

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter

(to keep things simple let it only be ‘+’, ‘-’ or ‘*’)

and an arbitrary number of arguments (only numbers) as the second parameter.

Then return the sum or product of all the numbers in the arbitrary parameter. For example:

'''

# сделал через IF-ы...
print('Insert "0" will exit from simple calculator!')
arithmetic_operator = input('Choose operation: +, -, *? ')
if arithmetic_operator == 0:
    pass
if arithmetic_operator in ('+', '-', '*'):
    x = int(input('x = '))
    y = int(input('y = '))
    if arithmetic_operator == '+':
        print('x + y = ' + str(x + y))
    elif arithmetic_operator == '-':
        print('x - y = ' + str(x - y))
    elif arithmetic_operator == '*':
        print('x * y = ' + str(x * y))
    else:
        print('Choose correct operation!')
