# Task 2
# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function

# Задача 2
# Создайте свою собственную реализацию встроенной функции range с именем in_range (),
# которая принимает три параметра: `start`,` end` и необязательный шаг.
# Советы: См. Документацию по функции `range`.

def in_range(start: int, end: int, step=1):
    while start < end:
        if end > 0 and step >= 0:
            yield start
            start = start + step

    while start > end:
        if end < 0 and step < 0:
            yield start
            start = start + step


if __name__ == '__main__':
    q = in_range(7, -18, -6)
    for el in q:
        print(el)


