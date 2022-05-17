"""
Your task is to make a program takes in a sentence (without puncuation), adds all words to a list and returns the sentence as a string which is the positions of the word in the list. Casing should not matter too.

Example
"Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"

becomes

"01234567802856734"

Another example
"the one bumble bee one bumble the bee"

becomes

"01231203"
"""


def compress(sentence):
    sentence = sentence.lower().split()
    new_sentence = []
    for i in sentence:
        if i not in new_sentence:
            new_sentence.append(i)
    hash_table = {}
    for index, i in enumerate(new_sentence):
        hash_table[i] = str(index)

    return "".join(hash_table[i] for i in sentence)
