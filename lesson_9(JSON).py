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


with open('myfile.txt') as hello:# считываем файл myfile.txt
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

# ne cdelal poisk po name/city/number, ne ycpevayu, budu delat' next zadaniya=)
# dobavlenie i ydaleniye rabotayut otlichno!!!
import json


def add_contact():
    phonebook.append(contact)
    return phonebook


def del_contact():
    phonebook.remove(contact)
    return phonebook


user_operation = input('Choose operation:\n'
                       '1 - for Add contact;\n'
                       '2 - for delete contact;\n')
first_name = input('Insert first name: ').lower()
last_name = input('Insert last name: ').lower().title()
phone_number = input('Insert phone number: ')
city = input('Insert city: ').lower().title()
full_name = first_name + last_name
contact = {full_name: {'first_name': first_name, 'lastname': last_name, 'phone': phone_number, 'city': city}}
phonebook = []
if __name__ == '__main__':
    if user_operation == '1':
        with open('phonebook.json', 'r') as file:
            phonebook = json.load(file)
        add_contact()
        with open('phonebook.json', 'w') as file:
            json.dump(phonebook, file, indent=2)

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