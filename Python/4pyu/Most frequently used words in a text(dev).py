# https://www.codewars.com/kata/51e056fe544cf36c410000fb
def top_3_words(text):
    text = text.lower().strip()

    valid_characters = " 'abcdefghijklmnopqrstuvwxyz"

    invalid_characters = {x for x in text if x not in valid_characters}

    aaa = "".join([x for x in text if x.isalpha()])
    if not aaa:
        return []
    text = text.split()

    text = list(map(lambda z: z.strip(), text))

    for x in invalid_characters:
        text = list(map(lambda z: z.replace(x, ""), text))

    text = [x for x in text if (x.isalpha() and "'" not in x) or (not x.isalpha() and "'" in x)]

    most_common = [(text.count(x), x) for x in set(text)]

    most_common = sorted(most_common, key=lambda x: x[0], reverse=True)

    return [x[1] for x in most_common[0:3]]


print(top_3_words("  //wont won't won't "))
# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words("  '  "))
# print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income."""))
# print(top_3_words("  , e   .. "))

if __name__ == "__main__":
    string = "FYw .-:nFnXDzCcFx;ksB;FYw_FYw/,!/FYw!ksB;,nFnXDzCcFx:_ksB!FYw;!,?kyIo:;:_ksB;,-kyIo? _ ?nFnXDzCcFx_ksB/kyIo -?/;nFnXDzCcFx.:.-FYw_nFnXDzCcFx /nFnXDzCcFx?/ __ksB_- nFnXDzCcFx/?.FYw:,.!:FYw_-_:-nFnXDzCcFx/kyIo/kyIo.ksB_:nFnXDzCcFx/-:nFnXDzCcFx-FYw!.:ksB-nFnXDzCcFx!/.;/kyIo/ ,,FYw  -.;ksB;-ksB/,ksB?! ,kyIo!!; ,ksB_!?nFnXDzCcFx:; ,:ksB:;- ksB.ksB_:ksB ?.,kyIo: ,nFnXDzCcFx!;/!FYw-?!kyIo-- :kyIo_,;ksB_kyIo!??. ksB:FYw _/ksB/:,kyIo.?_;,nFnXDzCcFx,,/ksB_;.:FYw-_ ::kyIo,ksB;,:-nFnXDzCcFx!:-kyIo-?!nFnXDzCcFx?-_ksB.FYw/nFnXDzCcFx!  ?;ksB,FYw,FYw/ /._ksB?nFnXDzCcFx:ksB_ !;/FYw:/ nFnXDzCcFx ,nFnXDzCcFx: ::kyIo/,,nFnXDzCcFx: ksB FYw-;FYw,ksB -/_,kyIo -:FYw!_;?ksB/_?;.nFnXDzCcFx_"
    print(string)
    a = [x if x in " 'abcdefghijklmnopqrstuvwxyz" else " " for x in string.lower()]
    print("".join(a))
