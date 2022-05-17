# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c


def max_sequence(arr):
    if not arr:
        return 0
    maximum = 0
    for start in range(len(arr)):
        for end in range(1, len(arr)):
            current_sequence = arr[start : end + 1]
            current_sum_of_sequence = sum(current_sequence)
            if current_sum_of_sequence > maximum:
                maximum = current_sum_of_sequence
    return maximum
