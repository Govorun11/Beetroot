# Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
# def stop_words(words: list):
#     pass
# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!
from functools import wraps


def stop_words(words: list):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            string = func(*args, **kwargs)
            for word in words:
                string = string.replace(word, '*')
            return string

        return wrapper

    return inner


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'


print(create_slogan('Steve'))
