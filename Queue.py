class List_New(list):
    @property
    def last_index(self):
        return len(self) - 1

    def __gt__(self, other):
        return len(self) > other


class Queue:
    def __init__(self):
        self.contents = List_New()

    def enqueue(self, item):
        self.contents.append(item)

    def dequeue(self):
        return None if len(self.contents) < 1 else self.contents.pop(0)

    def size(self):
        return len(self.contents)

    def __repr__(self):
        return self.contents

    def __str__(self):
        return str(self.contents)

    def __bool__(self):
        return bool(self.contents)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())