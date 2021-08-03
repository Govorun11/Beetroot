phonebook: list = []


def add_contact(name: str, number: str) -> list:
    contact: tuple = name, number
    phonebook.append(contact)
    return phonebook


def del_contact(name: str, number: str) -> list:
    contact: tuple = name, number
    phonebook.remove(contact)
    return phonebook
