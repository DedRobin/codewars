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
    compressing=[]
    index=0
    while index!=len(sentence):
        # a=sentence[index]
        if sentence.index(sentence[index]) in compressing:
            compressing.append(sentence.index(sentence[index]))
            sentence.pop(index)
        else:
            compressing.append(index)
            index+=1
    return ''.join(map(lambda x: str(x),compressing))

# print('012345617891011'==compress('The number 0 is such a strange number Strangely it has zero meaning'))
print(compress('The number 0 is such a strange number Strangely it has zero meaning'))
