# https://www.codewars.com/kata/52fba2a9adcd10b34300094c

def transpose(matrix):
    # We need to create list.
    # So we create the first row from the first column of matrix.
    new_matrix = [[x.pop(0) for x in matrix]]

    # Then we add other lines from matrix.
    # The loop will work until length of first nested lists is equal to zero.
    while len(matrix[0]) > 0:
        new_matrix.append([x.pop(0) for x in matrix])
    return new_matrix


# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]))
# print(transpose([[1, 2, 3]]))
print(transpose([[2, 4, 3, 2], [3, 2, 1, 3]]))
