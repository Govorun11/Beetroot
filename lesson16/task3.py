# Задача 3
# Создайте свою собственную реализацию итерации, которую можно использовать внутри цикла for-in.
# Также добавьте логику для извлечения элементов с использованием синтаксиса квадратных скобок.

# Task 3
# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.


def my_generator(*args):
    x = 10
    my_iter = iter(args)
    while x == 10:
        z = next(my_iter)
        yield z
        if z == args[-1]:
            x += 1


for i in my_generator(1, 2, 3, '5qwe'):
    print(i)
