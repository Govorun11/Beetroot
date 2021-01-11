'''
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
'''
#мне кажется, я не совсем понял все задание))

def oops():
    my_list = ['1', '2', 'error']
    my_index = my_list[3]
    print(my_index)

try:
    oops()
except IndexError:
    print('Max index less than specified!')

'''
Task 2

Write a function that takes in two numbers from the user via input(), 
call the numbers a and b, and then returns the value of squared a divided by b, 
construct a try-except block which raises an exception if the two values given by the input function were not numbers, 
and if value b was zero (cannot divide by zero).
'''


def abc():
    try:
        a = int(input('Insert first number: '))
        b = int(input('Insert second number: '))
        c = a ** 2 / b
        print(c)
    except ValueError:
        print('Insert int numbers!...')
    except ZeroDivisionError:
        print('cannot divide by zero')


abc()
