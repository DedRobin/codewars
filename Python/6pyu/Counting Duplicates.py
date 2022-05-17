"https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1"

from collections import Counter


def duplicate_count(text):
    duplicates = Counter(text.lower()).items()
    return sum([1 for x in duplicates if x[1] > 1])
