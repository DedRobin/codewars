# https://www.codewars.com/kata/55f2b110f61eb01779000053
def get_sum(a, b):
    return list(range(a, b + 1)) if a <= b else list(range(b, a + 1))