'''
Задача 3
Дробная часть
Создайте класс Fraction, который будет представлять всю базовую арифметическую логику для дробей (+, -, /, *)
с соответствующей проверкой и обработкой ошибок.
x = Fraction(1/2)

y = Fraction(1/4)

x + y == Fraction(3/4)
'''


class Fraction:
    def __init__(self, value: float):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    def __str__(self):
        return f'{self.value}'

    # def __key(self):
    #     return self.value

    def __eq__(self, other):
        return self.value == other.value

    def plus(self, fraction):
        self.value += fraction.value
        return self

    def minus(self, fraction):
        self.value -= fraction.value
        return self

    def div(self, fraction):
        if fraction.value != 0:
            self.value /= fraction.value
        else:
            raise ZeroDivisionError
        return self

    def mult(self, fraction):
        self.value *= fraction.value
        return self


x = Fraction(1 / 2)
y = Fraction(1 / 4)
z = Fraction(3 / 4)
print(x.plus(y))
print(z == x)
print(x.minus(y))
print(x.div(y))
print(x.mult(y))
