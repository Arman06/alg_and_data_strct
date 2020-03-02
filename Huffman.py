from MinHeap import Heap as PriorityQueue


class HuffmanTree:
    class Node:
        def __init__(self, value=None, frequency=None,  l_child=None, r_child=None):
            self.value = value
            self.frequency = frequency
            self.l_child = l_child
            self.r_child = r_child

        def __eq__(self, other):
            return self.frequency == other

        def __lt__(self, other):
            return self.frequency < other

        def __le__(self, other):
            return self.frequency <= other

        def __gt__(self, other):
            return self.frequency > other

        def __ge__(self, other):
            return self.frequency >= other

    def __init__(self):
        self.root = None

    def huffman_coding(self, symbols):
        nodes = []
        for symbol in symbols:
            nodes.append(self.Node(value=symbol[0], frequency=symbol[1]))
        queue = PriorityQueue(nodes)
        # print(nodes)
        while queue.contents > 1:
            # print("before deletion")
            # for node in queue.contents:
            #     print(node.frequency, end=" ")
            # print()
            node1 = queue.delete()
            node2 = queue.delete()
            # print("after deletion")
            # for node in queue.contents:
            #     print(node.frequency, end=" ")
            # print()
            parent_node = self.Node(value=None, frequency=(node1.frequency + node2.frequency),
                                    l_child=node2, r_child=node1)
            queue.insert(parent_node)
        self.root = queue.delete()
        print("done")
        return self.root

    def _get_code(self, cur_node, code="", codes_array=[]):
        if cur_node is not None:
            if cur_node.value is not None:
                print(cur_node.value)
                print(code)
                codes_array.append((cur_node.value, code))
            if cur_node.l_child is not None:
                code += "1"
                self._get_code(cur_node.l_child, code, codes_array)
            code = code[:-1]
            if cur_node.r_child is not None:
                code += "0"
                self._get_code(cur_node.r_child, code, codes_array)
        print(codes_array)

    def get_codes(self):
        if self.root is not None:
            self._get_code(self.root)

huf = HuffmanTree()
huf.huffman_coding([("a_1", 0.4), ("a_2", 0.15), ("a_3", 0.15), ("a_4", 0.15), ("a_5", 0.15)])
# print(huf.root.l_child.r_child.r_child.value)
huf.get_codes()