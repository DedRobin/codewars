"https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145"


def bingo(array):
    return (
        "WIN"
        if set(array) & set([2, 9, 14, 7, 15]) == set([2, 9, 14, 7, 15])
        else "LOSE"
    )


print(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]))
