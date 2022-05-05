'https://www.codewars.com/kata/52597aa56021e91c93000cb0'

def move_zeros(array):
    zeros=[0 for x in range(array.count(0))]
    array=list(filter(lambda x: x!=0,array))
    return array+zeros