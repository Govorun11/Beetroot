# Task 2
# Write tests for the Phonebook application, which you have implemented in module 1.
# Design tests for this solution and write tests using unittest library
phonebook = []


def add_contact(name, number):
    contact = name, number
    phonebook.append(contact)
    return phonebook


def del_contact(name, number):
    contact = name, number
    phonebook.remove(contact)
    return phonebook
