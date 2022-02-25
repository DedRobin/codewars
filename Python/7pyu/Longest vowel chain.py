import re

from numpy import mat
def solve(s):
    match=re.findall(r'[aeiou]+', s)
    return max(map(lambda x: len(x), match))

print(solve('codewarriors'))