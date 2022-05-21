# https://www.codewars.com/kata/54e6533c92449cc251001667
def unique_in_order(iterable):
    current_letter = None
    uniques = []
    for letter in iterable:
        print(letter, end=' ')
        if letter != current_letter:
            uniques.append(letter)
        current_letter = letter
    return uniques
