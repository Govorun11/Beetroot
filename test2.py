import unittest
import test


class NameTestCase(unittest.TestCase):

    def test_first_and_last_names(self):
        full = test.full_name('edik', 'kudryavcev')
        self.assertEqual(full, 'Edik Kudryavcev')


class AbcdTest(unittest.TestCase):

    def test_abcd(self):
        new_list = test.abcd(['q', 'w', 'e', 'r', 't'])
        self.assertEqual(new_list, ['qqq', 'www', 'eee', 'rrr', 'ttt'])



