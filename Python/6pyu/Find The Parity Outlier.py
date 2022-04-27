'https://www.codewars.com/kata/5526fc09a1bbd946250002dc'

def find_outlier(integers):
    print(integers)
    c_odd=0
    c_even=0
    for x in integers:
        if x%2:
            c_odd+=1
            odd=x
        else:
            c_even+=1
            even=x
        if (c_odd>1 and c_even==1):
            return even
        elif (c_odd==1 and c_even>1):
            return odd    