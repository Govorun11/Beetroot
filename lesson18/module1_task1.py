# Task 1
# Imports practice
# Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.
import datetime


def print_hello():
    today = datetime.date.today()
    print(f'Hello world! Today {str(today)}')

