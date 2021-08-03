import unittest
from lesson17 import task2


class TestPhonebook(unittest.TestCase):

    def test_add_contact(self):
        task2.add_contact('Edik', 12345)
        print(task2.phonebook)
        self.assertIn(('Edik', 12345), task2.phonebook)

    def test_del_contact(self):
        task2.del_contact('Edik', 12345)
        self.assertNotIn(('Edik', 12345), task2.phonebook)



