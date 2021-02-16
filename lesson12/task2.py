'''
Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
'''


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        for book in self.books:
            book.count = len(self.books)
        self.authors.append(author)

    def group_by_author(self):
        aut_list = {}
        for author in self.authors:
            aut_list[author] = [book for book in self.books if book.author is author]
        return aut_list

    def group_by_year(self, year):
        group_by_year = []
        for book in self.books:
            if book.year == year:
                group_by_year.append(book)
        return group_by_year


class Book:
    def __init__(self, name: str, year: int, author):
        self.name = name
        self.year = year
        self.author = author
        self.count = 0

    def __str__(self):
        return f'({self.author}) {self.name}, {self.year}, {self.count}'

    def __repr__(self):
        return f'({self.author}) {self.name}, {self.year}, {self.count}'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __repr__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def add_book(self, name):
        self.books.append(name)


a1 = Author('Ed', 'Ukr', 1999)
a2 = Author('Sla', 'Ukr', 1995)
library = Library("Kropivnitsky")
library.new_book("How much is fish", 1999, a1)
library.new_book('qwe', 2001, a1)
library.new_book('ert', 2004, a2)
library.new_book('ert', 2004, a2)
library.new_book('zcac', 2001, a1)
print(library.group_by_author())
# print(library.group_by_year(2001))
