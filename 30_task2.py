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
