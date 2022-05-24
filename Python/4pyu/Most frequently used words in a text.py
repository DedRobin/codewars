# https://www.codewars.com/kata/51e056fe544cf36c410000fb

from collections import Counter


def top_3_words(text):
    # I convert the string to lowercase.
    text = text.lower()

    # Using list comprehensions, we filter the string from characters we don’t need.
    valid_characters = " 'abcdefghijklmnopqrstuvwxyz"
    filter_text = [x if x in valid_characters else " " for x in text]

    # Then we combine the resulting list into a string and we split it.
    # We remove whitespace characters.
    filter_text = "".join(filter_text)
    filter_text = filter_text.split()

    # Create function which return True if string contain alphabet characters.
    def contain_alpha(string):
        for symbol in string:
            if symbol in "abcdefghijklmnopqrstuvwxyz":
                return True
        return False

    # Filter out our string and except characters which contain only apostrophe.
    filter_text = [x for x in filter_text if contain_alpha(x)]

    # Finally, we use Counter collection to find 3 top words in input text.
    most_common = Counter(filter_text).most_common(3)

    return [x[0] for x in most_common[0:3]]

# ---> Using import "collection.Counter" and "re"
#
# from collections import Counter
# import re
#
#
# def top_3_words(text):
#     c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
#     return [w for w,_ in c.most_common(3)]
