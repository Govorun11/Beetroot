class Animal:
    def __init__(self):
        pass


class Cat(Animal):
    def talk(self):
        print('Meow!')


class Dog(Animal):
     def talk(self):
         print('Woof!')


tom = Cat()
bob = Dog()
garfield = Cat()
animals = [tom, bob, garfield]
for animal in animals:
    animal.talk()
