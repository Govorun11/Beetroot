"""
Task 1

A Person class
Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
and add them as attributes.
Make another method called talk() which makes prints a greeting from the person containing, for example like this:
“Hello, my name is Carl Johnson and I’m 26 years old”.
"""


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


i_am = Person('Edik', 'Kudryavcev', '21')
print(f"Hello, my name is {i_am.firstname} {i_am.lastname} and i'm {i_am.age}!")
'''
Task 2

Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent
'''


class Dog:
    AGE_FACTOR = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.AGE_FACTOR


my_dog = Dog(9)
print(my_dog.human_age())

"""
Task 3

TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
if the channel N or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.
"""


class TVcontroller:
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    def __init__(self, this_channel):
        self.this_channel = this_channel

    def first_channel(self):
        self.this_channel = self.CHANNELS[0]
        return self.this_channel

    def last_channel(self):
        self.this_channel = self.CHANNELS[-1]
        return self.this_channel

    def turn_channel(self, channel_number):
        try:
            self.this_channel = self.CHANNELS[channel_number - 1]
            return self.this_channel
        except IndexError:
            print('У вас меньше каналов, чем вы указали...')

    def next_channel(self):
        if self.CHANNELS.index(self.this_channel) + 1 < len(self.CHANNELS):
            self.this_channel = self.CHANNELS[self.CHANNELS.index(self.this_channel) + 1]
            return self.this_channel
        return self.first_channel()

    def previous_channel(self):
        if self.CHANNELS.index(self.this_channel) >= 0:
            self.this_channel = self.CHANNELS[self.CHANNELS.index(self.this_channel) - 1]
            return self.this_channel
        return self.last_channel()

    def current_channel(self):
        return f'This channel is {self.this_channel}'


if __name__ == '__main__':
    controller = TVcontroller(1)
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.turn_channel(1))
    print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.current_channel())
