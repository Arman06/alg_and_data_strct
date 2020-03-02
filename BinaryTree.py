class BinarySearchTree:
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.r_child = None
            self.l_child = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.l_child is None:
                current_node.l_child = self.Node(value)
            else:
                self._insert(value, current_node.l_child)
        elif value > current_node.value:
            if current_node.r_child is None:
                current_node.r_child = self.Node(value)
            else:
                self._insert(value, current_node.r_child)
        else:
            print('duplicates')

    # def print(self):
    #