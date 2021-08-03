# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."
from collections import deque


def brackets_balance(chars: str):
    queue = deque()
    valid_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in chars:
        if char in valid_brackets.values():
            queue.append(char)
        if char in valid_brackets:
            try:
                if valid_brackets[char] != queue.pop():
                    return False
            except IndexError:
                return False
    return True


if __name__ == '__main__':
    print(brackets_balance('[[{()}]]'))
    print(brackets_balance('([{]})'))
    print(brackets_balance('()'))
    print(brackets_balance('({])'))
    print(brackets_balance('((()))'))
