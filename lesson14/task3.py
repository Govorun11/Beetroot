# Task 3
# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False,
# the function should return False and print the reason it failed; otherwise, return the result.

# def arg_rules(type_: type, max_length: int, contains: list):
#     pass
#
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
# assert create_slogan('johndoe05@gmail.com') is False
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
from functools import wraps

def arg_rules(max_lenght: int, type_: str, contains: list):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            checking = func(*args, **kwargs)
            for el in contains:
                if el in checking:
                    if len(checking) < max_lenght and type(type_) is str:
                        return f'{checking} drinks pepsi in his brand new BMW!'
            else:
                return False

        return wrapper

    return inner


@arg_rules(15, ' ', ['05', '@'])
def create_slogan(name: str):
    return f'{name}'


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
