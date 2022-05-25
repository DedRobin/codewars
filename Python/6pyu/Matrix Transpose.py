# https://www.codewars.com/kata/52fba2a9adcd10b34300094c

def transpose(matrix):
    new_matrix = [None] * min(len(matrix), len(matrix[0]))
    if len(matrix) == 0:
        return []
    if len(matrix) == 1:
        return [[y] for y in matrix[0]]
    for i in range(len(new_matrix)):
        new_matrix[i] = [z[i] for z in matrix]
    return new_matrix


# print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]))
print(transpose([[1, 2, 3]]))
print([[2, 4, 3, 2], [3, 2, 1, 3]])
