import re

def solve(s):
    match=re.findall(r'[aeiou]+', s)
    return max(map(lambda x: len(x), match))