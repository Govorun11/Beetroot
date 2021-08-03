class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def get_from_stack(self, needed_elem):
        new_stack = Stack()
        elem = ''
        while self.items:
            elem = self.pop()
            if elem == needed_elem:
                break
            else:
                new_stack.push(elem)

        while new_stack.items:
            self.push(new_stack.pop())

        if elem != needed_elem:
            raise ValueError(f'{needed_elem} NOT FOUND!')
        del new_stack
        return self.items


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.get_from_stack(1))
print(s.get_from_stack(2))
print(s.get_from_stack(5))
