# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function

# Создайте свою собственную реализацию встроенной функции enumerate с именем `with_index`,
# которая принимает два параметра:` iterable` и `start`, по умолчанию 0.
# Советы: см. Документацию по функции enumerate.

my_list = ['qwe', 'ert', 'rty', 'zxc']


def with_index(iterable, start=0):
    for el in iterable:
        yield el, start
        start += 1


s = with_index(my_list)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
