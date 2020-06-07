from itertools import combinations


def distance(codes):
    return min(sum(bit1 != bit2 for bit1, bit2 in zip(code1, code2)) for code1, code2 in combinations(codes, 2))


def detected(hdistance):
    return hdistance - 1


def correct(hdistance):
    return (hdistance - 1) / 2


codes_array1 = ['11110', '01011', '00000', '10101']
codes_array2 = ['01010', '10100', '00001', '11111']
distance1, distance2 = distance(codes_array1), distance(codes_array2)
print(distance1, distance2)
print(detected(distance1), detected(distance2))
print(correct(distance1), correct(distance2))


