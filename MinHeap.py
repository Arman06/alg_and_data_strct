class List_New(list):
    @property
    def last_index(self):
        return len(self) - 1

    def __gt__(self, other):
        return len(self) > other


class Heap:
    def __init__(self, items=[]):
        self.contents = List_New()
        for item in items:
            self.contents.append(item)
            self.heapify_up()

    def __bool__(self):
        return bool(self.contents)

    @property
    def last(self):
        return self.contents.last_index

    def last_element(self):
        return self.contents[self.last]

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return (i - 1)//2

    def heapify_up(self):
        new = self.last
        while new >= 1:
            parent = self.parent(new)
            if self.contents[new] < self.contents[parent]:
                self.contents[new], self.contents[parent] = self.contents[parent], self.contents[new]
                new = parent
            else:
                return

    def search(self, node):
        return self.contents.index(node)

    def insert(self, item):
        self.contents.append(item)
        self.heapify_up()

    def delete(self, node=None):
        if node is None:
            root = self.contents[0]
            self.contents[0], self.contents[self.last] = self.contents[self.last], self.contents[0]
            self.contents.pop()
            self.heapify_down()
            return root
        else:
            index = self.search(node)
            self.contents[index], self.contents[self.last] = self.contents[self.last], self.contents[index]
            self.contents.pop()
            self.heapify_down(index)

    def heapify_down(self, index=0):
        mini = index
        while index < len(self.contents):
            left = self.left_child(index)
            right = self.right_child(index)
            if left < len(self.contents) and right < len(self.contents):
                if self.contents[right] < self.contents[left]:
                    min_child_index = right
                else:
                    min_child_index = left
                if self.contents[min_child_index] < self.contents[index]:
                    mini = min_child_index
            elif left < len(self.contents):
                if self.contents[left] < self.contents[index]:
                    mini = left
            if index == mini:
                return
            self.contents[index], self.contents[mini] = self.contents[mini], self.contents[index]
            index = mini

    def peek(self):
        return self.contents[0]


if __name__ == "__main__":
    # heap = Heap([0.15, 0.15, 0.15, 0.4, 0.15])
#     # print(heap.contents)
#     # print(heap.peek())
#     # # heap.insert(10)
#     # # heap.insert(1)
#     # # heap.insert(1)
#     # # heap.insert(0)
#     # print(heap.contents)
#     # print(heap.peek())
#     # heap.delete()
#     # print(heap.contents)
#     # heap.delete()
#     # print(heap.contents)
#     # heap.delete()
#     # print(heap.contents)
#     # heap.insert(0.3)
#     # heap.insert(0.3)
#     # heap.delete()
#     # print(heap.contents)
#     # heap.delete()
#     # print(heap.contents)
    heap = Heap([0.125, 0.125, 0.25, 0.25, 0.125, 0.625, 0.625])
    print(heap.contents)
    heap.delete()
    print(heap.contents)
    heap.delete()
    print(heap.contents)
