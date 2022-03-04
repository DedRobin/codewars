"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""

def solution(args):
    start=args[0]
    end=0
    new_array=[]
    for index,i in enumerate(args[1:],1):
        if index==len(args)-1:
            end=i
            new_array.append('-'.join(map(str,[start,end])))
        elif (i-args[index-1])!=1:
            if start==end:
                new_array.append(str(start))
                start=i
            else:
                new_array.append('-'.join(map(str,[start,end])))
                start=i
        else:
            end=i
    return ','.join(new_array)
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))