class Stack:

    def __init__(self):
        self.content = []

    def pop(self):
        return self.content.pop() if len(self.content) >= 1 else None

    def push(self, item):
        self.content.append(item)

    def size(self):
        return len(self.content)

    def __repr__(self):
        return self.content

    def __str__(self):
        return str(self.content)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack)
