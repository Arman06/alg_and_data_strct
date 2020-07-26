import itertools


def ToReducedRowEchelonForm(matrix):
    if not matrix:
        return
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_index = column_count - row_count
#   pivot_index = 0
    for current_row_index in range(row_count):
        for rw in matrix:
            for n in rw:
                print('{:.1f}'.format(n + 0), end=" ")
            print()
        print()
        if pivot_index >= column_count:
            return
        swap_row_index = current_row_index
        while matrix[swap_row_index][pivot_index] == 0:
            swap_row_index += 1
            if swap_row_index == row_count:
                swap_row_index = current_row_index
                pivot_index += 1
                if column_count == pivot_index:
                    return
        matrix[swap_row_index], matrix[current_row_index] = matrix[current_row_index], matrix[swap_row_index]
        pivot_var = matrix[current_row_index][pivot_index]
        matrix[current_row_index] = [current_row_var / float(pivot_var) for current_row_var in matrix[current_row_index]]
        for remaining_row_index in range(row_count):
            if remaining_row_index != current_row_index:
                pivot_var = matrix[remaining_row_index][pivot_index]
                matrix[remaining_row_index] = [remaining_row_var - pivot_var * current_row_var
                                               for current_row_var, remaining_row_var in
                                               zip(matrix[current_row_index], matrix[remaining_row_index])]
        pivot_index += 1
        print(pivot_index)
        print(current_row_index)


mtx = [ [1, 2, -1, -4, 2],
        [2, 3, -1, -11, 2],
        [-2, 0, -3, 22, 2]]


ToReducedRowEchelonForm(mtx)
for rw in mtx:
    for n in rw:
        print('{: .1f}'.format(n + 0), end=" ")
    print()


F = [list(i) for i in itertools.product([0, 1], repeat=6)]
print(F)

for row in [*zip(*F)]:
    for el in row:
        print('{:1}'.format(el), end=" ")
    print()
