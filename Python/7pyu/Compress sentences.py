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
    sentence=sentence.lower().split()
    indexes=[]
    count=0
    for index,word in enumerate(sentence):
        if index!=sentence.index(word):
            indexes.append(sentence.index(word))
            count+=1
        else:
            indexes.append(sentence.index(word)-count)
    print(indexes)
    return indexes
print('012345617891011'==compress('The number 0 is such a strange number Strangely it has zero meaning'))
