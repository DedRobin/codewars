"https://www.codewars.com/kata/576bb71bbbcf0951d5000044"


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    else:
        positives = 0
        sum_negatives = 0
        for i in arr:
            if i > 0:
                positives += 1
            if i < 0:
                sum_negatives += i
        return [positives, sum_negatives]
