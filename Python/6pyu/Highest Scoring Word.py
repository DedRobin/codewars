'https://www.codewars.com/kata/57eb8fcdf670e99d9b000272'

def high(sentence):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    list_of_words=sentence.split()
    highest_score=0
    curent_word=list_of_words[0]
    for word in list_of_words:
        curent_score=sum([alphabet.index(letter)+1 for letter in word])
        if curent_score>highest_score:
            highest_score=curent_score
            curent_word=word
    return curent_word