#https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    r,g,b=(0 if num<0 else num for num in (r,g,b))
    r,g,b=(255 if num>255 else num for num in (r,g,b))
    return ('{:02X}'*3).format(r,g,b)

# print(rgb(-1,0,257))