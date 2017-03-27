import sys


class Stack:
    def __init__(self, stack):
        self.stack = list(stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return ' '.join(str(obj) for obj in self.stack)


exec (sys.stdin.read())
