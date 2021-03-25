import unittest
from lesson17 import ForTask1


class PersonTest(unittest.TestCase):

    def test_person(self):
        pers_name_age = ForTask1.person('Dasha', 22)
        self.assertEqual(pers_name_age, 'Dasha, 22')


class AbcdTest(unittest.TestCase):

    def test_abcd(self):
        new_list = ForTask1.abcd(['q', 'w', 'e', 'r', 't'])
        self.assertEqual(new_list, ['qqq', 'www', 'eee', 'rrr', 'ttt'])


unittest.main()

