'''
Task 1

School

Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher.
'''


class Person:
    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age

    def show_person(self):
        return f'Person: {self.name}, Gender: {self.gender}, Age: {str(self.age)}'


class Student(Person):
    def __init__(self, gender, name, age, course, marks):
        super().__init__(gender, name, age)
        self.course = course
        self.marks = marks

    def new_marks(self, **kwargs):
        self.marks = dict(kwargs)
        return self.marks

    def show_student(self):
        return f'NameStudent: {self.name}, genderStudent: {self.gender}, AgeStudent: {self.age}, ' \
               f'CourseStudent: {str(self.course)}, MarksStudent: {str(self.marks)}'

    def next_course(self):
        self.course += 1
        return str(self.course)


class Teacher(Person):
    def __init__(self, gender, name, age, classroom, salary):
        super().__init__(gender, name, age)
        self.salary = salary
        self.classroom = classroom

    def teacher(self):
        return f'{self.name}, {self.gender}, {self.age}, {self.classroom}, {self.salary}'

    def increase_salary(self, percent):
        self.salary = self.salary + self.salary / 100 * percent
        return str(self.salary)

    def decrese_salary(self, percent):
        self.salary = self.salary - self.salary / 100 * percent
        return str(self.salary)

    def change_classroom(self, new_classroom):
        self.classroom = new_classroom
        return str(self.classroom)


if __name__ == '__main__':
    person = Person('man', 'Edik Kudryavcev', 21)
    student = Student('Man', 'Edik Kudryavcev', 21, 4, {})
    teacher = Teacher('Women', 'Darya Ivanova', 'Age: ' + str(22), 'Classroom №' + str(121), 5000)
    print(person.show_person())
    print(student.new_marks(math=3, ukrLang=4, litr=5, biol=4))
    teacher.increase_salary(10)
    print(teacher.teacher())
    teacher.decrese_salary(20)
    print(teacher.teacher())
    teacher.change_classroom('Classroom №' + str(333))
    print(teacher.teacher())
    student.next_course()
    print(student.show_student())

'''
Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
    square_nums (takes a list of integers and returns the list of squares)
    remove_positives (takes a list of integers and returns it without positive numbers
    filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:
    pass

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
'''


class Calculator:
    list_for_square = [7, 11, 5, 4]
    list_for_remove = [26, -11, -8, 13, -90]
    years = [2001, 1884, 1995, 2003, 2020]


class Matematician(Calculator):

    def square_nums(self):
        list_of_squares = [number ** 2 for number in math.list_for_square]
        return list_of_squares

    def remove_pozitives(self):
        remove_poz = [number for number in math.list_for_remove if number <= 0]
        return remove_poz

    def filter_leaps(self):
        leap_years = []
        for year in math.years:
            if year % 4 == 0 or (year % 400 != 0 and year % 100 == 0):
                leap_years.append(year)
        return leap_years


if __name__ == '__main__':
    math = Matematician()
    print(math.square_nums())
    print(math.remove_pozitives())
    print(math.filter_leaps())

'''
Магазин продуктов
Напишите класс Product с тремя атрибутами:
тип
имя
цена
Затем создайте класс ProductStore, который будет иметь несколько продуктов и будет работать со всеми продуктами в магазине.
Все методы, если они не могут выполнить свое действие, должны вызывать ValueError с соответствующей информацией об ошибке.
Советы: используйте концепции агрегирования / композиции при реализации класса ProductStore.
Вы также можете реализовать дополнительные классы для работы с определенным типом продукта и т. Д.
Также класс ProductStore должен иметь следующие методы:

add (product, amount) - добавляет указанное количество одного товара с предопределенной ценовой надбавкой для вашего магазина (30 процентов)
set_discount (идентификатор, процент, identifier_type = 'name') - добавляет скидку на все товары,
указанные входными идентификаторами (тип или имя). Скидка должна быть указана в процентах.
sell_product (product_name, amount) - удаляет определенное количество товаров из магазина, если они есть, в противном случае вызывает ошибку.
Он также увеличивает доход, если метод sell_product завершается успешно.
get_income () - возвращает сумму многих заработанных экземпляром ProductStore.
get_all_products () - возвращает информацию обо всех доступных в магазине товарах.
get_product_info (product_name) - возвращает кортеж с названием продукта и количеством товаров в магазине.
'''
import json


# работает не все...


class Product:
    def __init__(self, group, name, price):
        self.group = group
        self.name = name
        self.price = price

    # def set_discount(self, discount):
    #     self.price -= self.price/100*discount

    def __str__(self):
        return f'{self.group}, {self.name}, {self.price}'

    def __repr__(self):
        return self.__str__()


class ProductStore:
    def __init__(self):
        self.all_prod = {}

    def add_product(self, product, amount):
        self.upload()
        if product in self.all_prod:
            qty = self.all_prod[product]
            new_amount = qty + amount
            self.all_prod[product] = new_amount
        else:
            self.all_prod[product] = amount
        self.reload()
        return self.all_prod

    def sell_product(self, product, amount):
        self.upload()
        qty = self.all_prod[product]
        new_amount = qty - amount
        if new_amount >= 0:
            self.all_prod[product] = new_amount
            self.reload()
        else:
            raise ValueError('Amount less then insert')
        return self.all_prod

    def get_income(self):
        pass

    def get_all_products(self):
        return self.upload()

    def get_product_info(self, product):
        self.upload()
        qty = self.all_prod[product]
        return product, qty

    def upload(self):
        with open('ProdStore.json', 'r') as file:
            self.all_prod = json.load(file)
        return self.all_prod

    def reload(self):
        with open('ProdStore.json', 'w') as file:
            json.dump(self.all_prod, file, indent=2)


if __name__ == '__main__':
    product1 = Product('Food', 'apple', 2)
    product2 = Product('Kanc', 'Pen', 10)
    s = ProductStore()
    print(s.get_all_products())
    s.add_product(str(product1), 15)
    s.add_product(str(product2), 10)
    s.sell_product(str(product2), 10)
    s.sell_product(str(product1), 12)
    print(s.get_all_products())
