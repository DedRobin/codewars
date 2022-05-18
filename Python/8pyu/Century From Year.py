# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
def century(year):
    return year // 100 + 1 if year % 100 else year // 100
