'''
Task 1

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.

The function should then print “My favorite movie is named {name}”.
'''

def favourite_movie():
    name = input('What is your favourite movie? ')
    print(f'My favorite movie is named "{name.title()}"!')
favourite_movie()