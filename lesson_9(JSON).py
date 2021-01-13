'''
Task 1

Files

Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents.
Run your two scripts from the system command line.
Does the new file show up in the directory where you ran your scripts?
What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings;
add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.
'''



h = 'Hello file world!'
with open('myfile.txt', 'w') as hello: # записываем значение переменной h в новый файл myfile.txt;
    hello_file_world = hello.write(h)
print(hello_file_world)


with open('myfile.txt') as hello: # считываем файл myfile.txt
    hello_file_world = hello.read()
print(hello_file_world)



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

new_contact = {}
print('Delete contact - 1, Update contact - 2, Add contact - 3')
user_operation = input('What do you want to do? ')
firstname = input('Insert your first name:').lower().title()
lastname = input('Insert your last name: ').lower().title()
fullname = str(firstname + ' ' + lastname)
phone_number = input('Insert phone number:')
city = input('Insert your city: ').lower().title()


def add_contact():
    new_contact[fullname] = {'firstname': firstname, 'lastname': lastname, 'phone': phone_number, 'city': city}
    return new_contact


def del_contact():
    del new_contact[fullname]
    return new_contact


def update_contact():
    del_contact()
    new_contact[fullname] = {'firstname': firstname, 'lastname': lastname, 'phone': phone_number, 'city': city}
    return new_contact


if user_operation == '1':
    if fullname in new_contact:
        del_contact()
elif user_operation == '2':
    update_contact()
elif user_operation == '3':
    add_contact()
else:
    print('Choose correct operation!...')
with open('phonebook.json', 'a') as file:
    json.dump(new_contact, file, indent=2)
