class ShannonFano:
    class Node:
        def __init__(self, value=None, frequency=None, l_child=None, r_child=None):
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

    def equal_sub_lists(self, li):
        one = []
        two = []
        print(li)
        if not all(li[i][1] <= li[i + 1][1] for i in range(len(li) - 1)):
            li.sort(key=lambda x: x[1], reverse=True)
        print(li)
        for el in li:
            if sum([pair[1] for pair in one]) > sum([pair[1] for pair in two]):
                two.append(el)
            else:
                one.append(el)
        print(one, "and", two)
        return two, one

    def _shannon_fano_coding(self, cur_node):
        if len(cur_node.value) > 1:
            left, right = self.equal_sub_lists(cur_node.value)
            cur_node.l_child = self.Node(left)
            cur_node.r_child = self.Node(right)
            self._shannon_fano_coding(cur_node.l_child)
            self._shannon_fano_coding(cur_node.r_child)

    def shannon_fano_coding(self, data):
        self.root = self.Node(value=data)
        self._shannon_fano_coding(self.root)

    def _get_code(self, cur_node, code="", codes_array=[]):
        if cur_node is not None:
            if len(cur_node.value) == 1:
                # print(cur_node.value)
                # print(code)
                codes_array.append((cur_node.value, code))
            if cur_node.l_child is not None:
                code += "1"
                self._get_code(cur_node.l_child, code, codes_array)
            code = code[:-1]
            if cur_node.r_child is not None:
                code += "0"
                self._get_code(cur_node.r_child, code, codes_array)
        return codes_array

    def get_codes(self):
        if self.root is not None:
            return sorted(self._get_code(self.root), key=lambda pair: pair[0])


source = [("a_1", 0.4), ("a_2", 0.15), ("a_3", 0.15), ("a_4", 0.15), ("a_5", 0.15)]
source1 = [("d", 0.3), ("b", 0.28), ("a", 0.22), ("c", 0.15), ("e", 0.05)]
shannon = ShannonFano()
shannon.shannon_fano_coding(source1)
print(shannon.root.r_child.value)
print(shannon.get_codes())