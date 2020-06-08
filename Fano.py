from math import log2


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
        # print(li, "lol")
        #
        # if not all(li[i][1] <= li[i + 1][1] for i in range(len(li) - 1)):
        #     li.sort(key=lambda x: x[1], reverse=True)
        # for el in li:
        #     if sum([pair[1] for pair in one]) > sum([pair[1] for pair in two]):
        #         two.append(el)
        #     else:
        #         one.append(el)
        # print(one, "and", two)
        li.sort(key=lambda x: x[1], reverse=True)
        # print(li)
        one = [li[0]]
        two = li[1:]
        # print(one, "and", two)
        print()
        for i in range(2, len(li)):
            test_one = li[0:i]
            test_two = li[i:]
            print(li)
            print("not test", one, "and", two)
            print("test", test_one, "and", test_two)
            current_sum = abs(sum([pair[1] for pair in one]) - sum([pair[1] for pair in two]))
            test_sum = abs(sum([pair[1] for pair in test_one]) - sum([pair[1] for pair in test_two]))
            print("sum", test_sum, current_sum)
            if test_sum > current_sum or current_sum == 0:
                print(one, "and confirm", two)
                return one, two
            one = test_one
            two = test_two
            print()
        print("final", one, two)
        return one, two

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
                codes_array.append((cur_node.value[0], code))
            if cur_node.l_child is not None:
                code += "0"
                self._get_code(cur_node.l_child, code, codes_array)
            code = code[:-1]
            if cur_node.r_child is not None:
                code += "1"
                self._get_code(cur_node.r_child, code, codes_array)
        return codes_array

    def get_codes(self):
        if self.root is not None:
            return sorted(self._get_code(self.root), key=lambda pair: pair[0])

    @staticmethod
    def entropy(symbols):
        return -sum([probability * log2(probability) for symbol, probability in symbols])

    @staticmethod
    def average_len(codes, symbols):
        return sum([probability[1] * len(symbol[1]) for symbol, probability in zip(codes, symbols)])


source = [("a_1", 0.4), ("a_2", 0.15), ("a_3", 0.15), ("a_4", 0.15), ("a_5", 0.15)]
# source1 = [("в", 0.25), ("е", 0.25), ("о", 0.125), ("п", 0.125), ("с", 0.125), ("т", 0.0625), ("ь", 0.0625)]
shannon = ShannonFano()
shannon.shannon_fano_coding(source)
codes = shannon.get_codes()
print(codes)
print("entropy is ", shannon.entropy(source))
print("average length is ", shannon.average_len(codes, source))
