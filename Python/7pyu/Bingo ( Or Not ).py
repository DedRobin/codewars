'https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145'

def bingo(array):
    return 'WIN' if set([chr(number+96) for number in array])&set(['b','i','n','g','o'])==set(['b','i','n','g','o']) else 'LOSE'

print(bingo([1, 2, 3, 7, 5, 14, 7, 15, 10]))