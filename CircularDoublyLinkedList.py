class CircularDoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.value = data
            self.next = None
            self.prev = None

        def __repr__(self):
            return str(self.value)

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.head = None
        self.tail = self.head  # unnecessary

    def traverse(self):
        if self.head is None:
            print("Nope")
            return
        else:
            print(self.head.value, end=" ")
            present_node = self.head.next
            while present_node is not self.head:
                print(present_node.value, end=" ")
                present_node = present_node.next
        print()

    def insert_start(self, data):
        new = self.Node(data)
        if self.head is None:
            self.head = new
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head
        else:
            new.next = self.head
            new.prev = self.tail
            self.head.prev = new
            self.head = new
            self.tail.next = new

    def append(self, data):
        new = self.Node(data)
        if self.head is None:
            self.head = new
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head
        else:
            new.prev = self.tail
            new.next = self.head
            self.tail.next = new
            self.tail = new
            self.head.prev = new

    @staticmethod
    def __remove_node__(node):
        previous = node.prev
        next_ = node.next
        previous.next = next_
        next_.prev = previous

    def remove_at_start(self):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

    def remove_at_end(self):
        if self.head is self.tail:
            self.head = self.tail = None
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail

    def remove_at(self, index):
        if index == 0:
            self.remove_at_start()
            return
        i = 1
        present_node = self.head.next
        while present_node is not self.tail:
            if i == index:
                self.__remove_node__(present_node)
                return
            present_node = present_node.next
            i += 1
        if i == index:
            self.remove_at_end()
            return
        print("index out of range")

    def __repr__(self):
        return "head is {0} and tail is {1}".format(self.head, self.tail)

    def __str__(self):
        return "head is {0} and tail is {1}".format(self.head, self.tail)

    def __getitem__(self, item):
        index = item
        i = 0
        if index == 0:
            return self.head
        i += 1
        present_node = self.head.next
        while present_node is not self.head:
            if i == index:
                return present_node
            present_node = present_node.next
            i += 1
        print("No such value")


def main():
    li = CircularDoublyLinkedList()
    li.insert_start(3)
    li.insert_start(2)
    li.append(4)
    li.append(5)
    print(li[3])
    li.traverse()
    # li.remove_at_start()
    li.remove_at(2)
    li.remove_at(1)
    li.remove_at(0)
    li.traverse()
    # print(li.head)
    # print(li.tail)

if __name__ == "__main__":
    main()
