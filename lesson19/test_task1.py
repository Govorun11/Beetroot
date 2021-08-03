from lesson19 import task1
import os.path

def test_act():
    assert task1.cm.act in ('r', 'w', 'a')

def test_file_exists():
    assert os.path.exists('diary.txt')



