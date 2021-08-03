import collections


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, *args):
        for el in args:
            self.items.append(el)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def get_from_queue(self, needed_elem):
        new_queue = collections.deque()
        elem = ''
        i = 0
        while self.items:
            elem = self.pop()
            if elem == needed_elem:
                i += 1
                del elem

            else:
                new_queue.appendleft(elem)

        if i == False:
            raise ValueError(f'{needed_elem} not found!')
        return new_queue


my_queue = Queue()
my_queue.push(1, 2, 3, 4, 5)
print(my_queue.get_from_queue(2))
