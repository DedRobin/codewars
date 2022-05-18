# https://www.codewars.com/kata/554e4a2f232cdd87d9000038
def DNA_strand(dna):
    dna = dna.translate(dna.maketrans('ACTG', 'TGAC'))
    return dna
