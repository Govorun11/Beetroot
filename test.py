'''
Task 2

Extend Phonebook application
Functionality of Phonebook application:

    Add new entries
    Search by first name
    Search by last name
    Search by full name
    Search by telephone number
    Search by city or state
    Delete a record for a given telephone number
    Update a record for a given telephone number
    An option to exit the program

The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application, else raise an error.
After the user exits, all data should be saved to loaded JSON.
'''
import json


def add_contact():
    phonebook.append(contact)
    return phonebook


def del_contact():
    phonebook.remove(contact)
    return phonebook

# def update_contact():
# #     update_contact = input('New first name is: ')
# #


user_operation = input('Choose operation:\n'
                       '1 - for Add contact;\n'
                       '2 - for delete contact;\n'
                       '3 - for update contact;\n')
first_name = input('Insert first name: ').lower()
last_name = input('Insert last name: ').lower().title()
phone_number = input('Insert phone number: ')
city = input('Insert city: ').lower().title()
full_name = first_name + last_name
contact = {full_name: {'first_name': first_name, 'lastname': last_name, 'phone': phone_number, 'city': city}}
phonebook = []
if user_operation == '1':
    if contact in phonebook == False:
        with open('phonebook.json', 'r') as file:
            phonebook = json.load(file)
        add_contact()
        with open('phonebook.json', 'w') as file:
            json.dump(phonebook, file, indent=2)
    else:
        print('This contact in phonebook!...')
elif user_operation == '2':
    with open('phonebook.json', 'r') as file:
        phonebook = json.load(file)
    del_contact()
    with open('phonebook.json', 'w') as file:
        json.dump(phonebook, file, indent=2)
elif user_operation == '3':
    del_contact()
else:
    print('Choose correct operation!...')
