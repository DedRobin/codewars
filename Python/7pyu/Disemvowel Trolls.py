"https://www.codewars.com/kata/52fba66badcd10859f00097e"


def disemvowel(s):
    return "".join([x for x in s if x.lower() not in ("a", "e", "i", "o", "u")])


print(disemvowel("LOl"))
