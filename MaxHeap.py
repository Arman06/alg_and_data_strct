class List_New(list):
    @property
    def last_index(self):
        return len(self) - 1


class Heap:
    def __init__(self, items=[]):
        self.contents = List_New()
        for item in items:
            self.contents.append(item)
            self.heapify_up()

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
            if self.contents[new] > self.contents[parent]:
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
            self.contents[0], self.contents[self.last] = self.contents[self.last], self.contents[0]
            self.contents.pop()
            self.heapify_down()
        else:
            index = self.search(node)
            self.contents[index], self.contents[self.last] = self.contents[self.last], self.contents[index]
            self.contents.pop()
            self.heapify_down(index)

    def heapify_down(self, index=0):
        maxi = index
        while index < len(self.contents):
            left = self.left_child(index)
            right = self.right_child(index)
            if left < len(self.contents):
                if self.contents[left] > self.contents[index]:
                    maxi = left
            elif right < len(self.contents):
                if self.contents[right] > self.contents[index]:
                    maxi = right
            if index == maxi:
                return
            self.contents[index], self.contents[maxi] = self.contents[maxi], self.contents[index]
            index = maxi

    def peek(self):
        return self.contents[0]


heap = Heap([1, 2, 3, 4, 9, 8, 7, 6])
print(heap.contents)
print(heap.peek())
heap.insert(10)
print(heap.contents)
print(heap.peek())
heap.delete()
print(heap.contents)
heap.delete(2)
print(heap.contents)
