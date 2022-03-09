"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""

#!!! not optimized

def solution(args):

    #start - used to register the starting position of a range of numbers
    #end - used to register the ending position of a range of numbers
    #count - used to calculate the difference 'start - i = 1'

    start=end=args[0]
    new_array=[]
    count=0

    for index,i in enumerate(args[1:],1):

        #for the last number in list
        #The ending position in range is 'i'. 'end' is the number before the last.
        
        if index==len(args)-1:
            if i-args[index-1]==1:
                count+=1
            if i-args[index-1]!=1:
                if count<1:
                    new_array.extend([str(start),str(i)])
                elif count==1:
                    new_array.extend([str(start),str(end)])
                    new_array.extend([str(i)])
                elif count>1:
                    new_array.append('-'.join([str(start),str(end)]))
                    new_array.extend([str(i)])
            elif i-args[index-1]==1:
                if count<1:
                    new_array.extend([str(start),str(i)])
                elif count==1:
                    new_array.extend([str(start),str(i)])
                elif count>1:
                    new_array.append('-'.join([str(start),str(i)]))
            else:
                new_array.append('-'.join([str(start),str(i)]))               
               
        elif i-args[index-1]==1:
            count+=1
            end=i
        else:
            if end-start==1 and count==1:
                new_array.extend([str(start),str(end)])
            elif count>1:
                new_array.append('-'.join([str(start),str(end)]))
            else:
                new_array.append(str(start))
            count=0
            start=i
    return ','.join(new_array)
