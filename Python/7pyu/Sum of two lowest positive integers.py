# https://www.codewars.com/kata/558fc85d8fd1938afb000014
def sum_two_smallest_numbers(numbers):
    numbers = sorted(list(filter(lambda x: x > 0 and type(x) == int, numbers)))
    return sum(numbers[:2])
