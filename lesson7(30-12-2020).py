'''
Task 1

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.

The function should then print “My favorite movie is named {name}”.
'''

def favourite_movie():
    name = input('What is your favourite movie? ')
    print(f'My favorite movie is named "{name.title()}"!')
favourite_movie()

'''
Task 2

Create a function called make_country, which takes in a country’s name and capital as parameters.

Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.

Make the function print out the values of the dictionary to make sure that it works as intended.
'''

country_name = input('Insert name of any country! ')
country_capital = input('Insert capital of this country! ')
country = {}
def make_country(name, capital): #add a key 'name', key 'capital' for dict country
    country['name'] = name
    country['capital'] = capital
    return country


print(make_country(country_name, country_capital))
print(country.values())

'''
TASK 3

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter

(to keep things simple let it only be ‘+’, ‘-’ or ‘*’)

and an arbitrary number of arguments (only numbers) as the second parameter.

Then return the sum or product of all the numbers in the arbitrary parameter. For example:

    the call make_operation(‘+’, 7, 7, 2) should return 16
    the call make_operation(‘-’, 5, 5, -10, -20) should return 30
    the call make_operation(‘*’, 7, 6) should return 42

'''


def make_operation(operation, *args):
    if operation in ('+', '-', '*'):
        summa = 0
        mul = 1
        if operation == '+':
            summa = 0
            for number in args:
                summa += number
            return summa
        elif operation == '-':
            summa = args[0]
            for number in args[1:]:
                summa -= number
            return summa

        else:
            for number in args:
                mul *= number
            return mul


print(make_operation('-', 5, 5, -10, -20))
