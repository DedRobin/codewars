#'https://www.codewars.com/kata/58539230879867a8cd00011c'


def find_children(s):
    return "".join(sorted(sorted(s), key=str.lower))
