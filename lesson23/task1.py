from collections import deque


def print_reversed_string(input_string: str):
    if not isinstance(input_string, str):
        try:
            input_string = str(input_string)
        except ValueError:
            raise ValueError('Input string must be a str() type!')

    my_stack = deque()
    reversed_string = str()
    for char in input_string:
        my_stack.append(char)
    while my_stack:
        reversed_string += my_stack.pop()
    print(reversed_string)
print_reversed_string(123455666)
print_reversed_string('Лепс спеЛ')
print_reversed_string([1,2,3,4])
