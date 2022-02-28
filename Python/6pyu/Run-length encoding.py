"""
Run-length encoding (RLE) is a very simple form of data compression in which runs of data (that is, sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run. Wikipedia

Task
Your task is to write such a run-length encoding. For a given string, return a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ], such that one can reconstruct the original string by replicating the character sx ix times and concatening all those strings. Your run-length encoding should be minimal, ie. for all i the values si and si+1 should differ.

Examples
As the article states, RLE is a very simple form of data compression. It's only suitable for runs of data, as one can see in the following example:
"""

def run_length_encoding(s):
    if not s: return []
    last_letter=s[0q]
    list_of_letters=[]
    count=0
    for index,letter in enumerate(s):
        if letter!=last_letter:
            list_of_letters.append([count,last_letter])
            last_letter=letter            
            count=1
        else:
            last_letter=letter 
            count+=1
    list_of_letters.append([count,last_letter])
    return list_of_letters