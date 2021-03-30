import sys


def count_lines(name):
    return len(open(name, 'r').readlines())


def count_chars(name):
    return len(open(name, 'r').read())


def test(file_name):
    return count_lines(file_name), count_chars(file_name)


if __name__ == '__main__':
    print(sys.argv)
    print(test(sys.argv[1]))