import unittest
import lesson17.ForTask1 as task1


class PersonNameAgeTest(unittest.TestCase):

    def test_person(self):
        pers_name_age = task1.person('dasha', '22')
        self.assertEqual(pers_name_age, 'Dasha 22')


class AbcdTest(unittest.TestCase):

    def test_abcd(self):
        new_list = task1.abcd(['q', 'w', 'e', 'r', 't'])
        self.assertEqual(new_list, ['qqq', 'www', 'eee', 'rrr', 'ttt'])



