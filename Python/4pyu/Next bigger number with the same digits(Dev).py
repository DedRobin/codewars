#https://www.codewars.com/kata/55983863da40caa2c900004e
import sys
def next_bigger(n):
    print(n)
    n = [int(x) for x in str(n)]
    r_n = n[::-1]
    print(n, r_n, sep = '\n')
    for index_1,num_1 in enumerate(r_n):        
        index_2=index_1+1
        try:            
            num_2 = r_n[index_2]
        except IndexError:
            return -1        
        if num_1 > num_2:
            r_n[index_1] = num_2
            r_n[index_2] = num_1
    return -1
# print(next_bigger(59884848459853))
print(next_bigger(31298))