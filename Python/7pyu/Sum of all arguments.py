"""
Write a function that finds the sum of all its arguments.

eg:

sum_args(1, 2, 3) # => 6
sum_args(8, 2) # => 10
sum_args(1, 2, 3, 4, 5) # => 15
"""

def sum_args(*arg):
    return sum(arg)