def to_power(x: [int, float], exp: int) -> [int, float]:
    if exp == 0:
        return 1
    if x == 0:
        return 0
    if exp <= 10:
        print(x ** exp)
        return to_power(x, exp - 1)


# print(to_power(3,10))

# Task2
# Checks if input string is Palindrome
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if isinstance(looking_str, str):
        if len(looking_str) == 1 or len(looking_str) == 0:
            return True
        if looking_str[0:1] == looking_str[-1:]:
            return is_palindrome(looking_str[1:-1])
        return False
    return False

# x = is_palindrome('12321')
# print(x)




# Task3
def mult(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("This function works only with postive integers")
    print(a * b)
    return mult(a, (b - 1))


# mult(3, 5)


# task4
def reverse(input_str: str) -> str:
    if input_str == '':
        return 'empty line'
    print(input_str[::-1])
    return reverse(input_str[0:-1])


# reverse(input('Your string: '))


def sum_of_digit(digit_string: str) -> int:
    if digit_string == 0:
        raise ValueError('empty line')
    if digit_string.isalpha():
        raise ValueError('input string must be digit string')
    if len(digit_string) == 0:
        return False
    return int(digit_string[0]) + sum_of_digit(digit_string[1:])


# x = sum_of_digit('1254')
# print(x)


