# https://www.codewars.com/kata/51e056fe544cf36c410000fb
def top_3_words(text):
    text = text.lower().strip()
    a = [32, 39] + list(range(97, 123))
    sym = {x for x in text if ord(x) not in a}
    contain_alpha = False
    contain_spec_symb = False
    for x in text:
        if ord(x) in a:
            check = True
            break
    if not check:
        return []
    for z in sym:
        text = text.replace(z, "")
    # list_with_words = (text.replace(x, "") for x in sym)
    list_with_words = text.split()
    set_with_words = set(text.split())
    result = [(text.count(word), word) for word in set_with_words]
    result = sorted(result, reverse=True)
    result = [x[1] for x in result][0:3]
    return result


# print(top_3_words("  //wont won't won't "))
# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words("  '  "))
# print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income."""))
