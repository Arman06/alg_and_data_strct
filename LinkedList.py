class LinkedList:

    class Node:
        def __init__(self, data=None):
            self.value = data
            self.ref = None

        def __repr__(self):
            return str(self.value)

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.first_node = None
        self.head = self.first_node
        self.tail = self.first_node

    def show(self):
        if self.first_node is None:
            print("Nope")
        else:
            present_node = self.first_node
            while present_node is not None:
                print(present_node.value, end=" ")
                present_node = present_node.ref
        print()

    def insert_start(self, data):
        new = self.Node(data)
        new.ref = self.first_node
        self.first_node = new
        self.head = self.first_node

    def insert_end(self, data):
        new = self.Node(data)
        if self.first_node is None:
            self.first_node = new
            return
        present_node = self.first_node.ref
        while present_node.ref is not None:
            present_node = present_node.ref
        present_node.ref = new
        # self.tail.ref = new
        # self.tail = new

    def __repr__(self):
        return "head is {0} and tail is {1}".format(self.head, self.tail)

    def __str__(self):
        return "head is {0} and tail is {1}".format(self.head, self.tail)

    def __getitem__(self, item):
        index = item
        i = 0
        present_node = self.first_node
        while present_node is not None:
            if i == index:
                return present_node
            present_node = present_node.ref
            i += 1
        print("No such value")


linked_list = LinkedList()
linked_list.insert_start("hello")
linked_list.insert_start("hi")
linked_list.insert_start(3)
linked_list.insert_start("pls")
linked_list.insert_start("stop")
linked_list.insert_end("end")
linked_list.insert_end("endd")
linked_list.show()
print(linked_list)
print(linked_list[6])


