"""
Motivation
When compressing sequences of symbols, it is useful to have many equal symbols follow each other, because then they can be encoded with a run length encoding. For example, RLE encoding of "aaaabbbbbbbbbbbcccccc" would give something like 4a 11b 6c.

(Look here for learning more about the run-length-encoding.)

Of course, RLE is interesting only if the string contains many identical consecutive characters. But what bout human readable text? Here comes the Burrows-Wheeler-Transformation.

Transformation
There even exists a transformation, which brings equal symbols closer together, it is called the Burrows-Wheeler-Transformation. The forward transformation works as follows: Let's say we have a sequence with length n, first write every shift of that string into a n x n matrix:

Input: "bananabar"

b a n a n a b a r
r b a n a n a b a
a r b a n a n a b
b a r b a n a n a
a b a r b a n a n
n a b a r b a n a
a n a b a r b a n
n a n a b a r b a
a n a n a b a r b
Then we sort that matrix by its rows. The output of the transformation then is the last column and the row index in which the original string is in:

               .-.
a b a r b a n a n
a n a b a r b a n
a n a n a b a r b
a r b a n a n a b
b a n a n a b a r <- 4
b a r b a n a n a
n a b a r b a n a
n a n a b a r b a
r b a n a n a b a
               '-'

Output: ("nnbbraaaa", 4)
Of course we want to restore the original input, therefore you get the following hints:

The output contains the last matrix column.
The first column can be acquired by sorting the last column.
For every row of the table: Symbols in the first column follow on symbols in the last column, in the same way they do in the input string.
You don't need to reconstruct the whole table to get the input back.
Goal
The goal of this Kata is to write both, the encode and decode functions. Together they should work as the identity function on lists. (Note: For the empty input, the row number is ignored.)
"""

def encode(s):
    #for empty string

    if s=='': return ('','')
    
    #creating the table

    s_copy=list(s)
    matrix=[]
    for i in range(len(s_copy)):
        matrix.append(''.join(s_copy))
        s_copy=s_copy.copy()        
        s_copy.insert(0,s_copy.pop())
    
    #sorting the table
    matrix.sort()

    #return encoded string and number
    encode_s=''.join([i[-1] for i in matrix])
    encode_index=matrix.index(s)

    return (encode_s,encode_index)

def decode(s, n):
    #for empty string or number
    if s=='' or n=='': return ''
    
    s=list(s)

    #s_sort    <---   This will be the last column in 'matrix'.
    s_sort=s.copy()

    s_sort.sort()

    #create the first column of last letters(s)
    matrix=[[letter] for letter in s_sort]

    #finding mathes
    #start with the first(0) column
    column=1
    while True:        
        for index,row in enumerate(matrix):

            #I created a variable "chunk" which consists of
            #this will be the last column of the variable "" + row "row".
            piece=s[index:index+1]+row[0:column]

            for row2 in matrix:
                if piece[:-1]==row2:
                    matrix[matrix.index(row2)]=piece
                    break
        column+=1
        
        if len(matrix[n])==len(s):
            return ''.join(matrix[n])