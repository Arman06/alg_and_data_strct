class Queue:
    def __init__(self):
        self.content = []

    def enqueue(self, item):
        self.content.append(item)

    def dequeue(self):
        return None if len(self.content) < 1 else self.content.pop(0)

    def size(self):
        return len(self.content)

    def __repr__(self):
        return self.content

    def __str__(self):
        return str(self.content)

    def __bool__(self):
        return bool(self.content)



if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())