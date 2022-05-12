#https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    r,g,b=(0 if num<0 else num for num in (r,g,b))
    r,g,b=(255 if num>255 else num for num in (r,g,b))
    return ''.join(['{:02X}'.format(num)for num in (r,g,b)])