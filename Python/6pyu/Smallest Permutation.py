"https://www.codewars.com/kata/5fefee21b64cc2000dbfa875"


def min_permutation(n: int):
    if n == 0:
        return 0
    minus = True if n < 0 else False
    lst = list(str(abs(n)))
    lst.sort()
    count_of_zero = lst.count("0")
    while lst[0] == "0":
        zero = lst.pop(0)
        lst.insert(count_of_zero, zero)
    n = int("".join(lst))
    return -n if minus else n
