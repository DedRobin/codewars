'https://www.codewars.com/kata/58539230879867a8cd00011c'
def find_children(dancing_brigade):
    dancing_brigade=sorted(dancing_brigade)
    all_letters=sorted(map(lambda x: x.lower(),dancing_brigade))
    upper_letters=[x for x in dancing_brigade if not x.islower()]
    for upper_letter in upper_letters:
        all_letters[all_letters.index(upper_letter.lower())]=upper_letter
    return ''.join(all_letters)