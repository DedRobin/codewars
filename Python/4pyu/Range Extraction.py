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
    start=end=args[0]
    new_array=[]
    count=0
    for index,i in enumerate(args[1:],1):
        if index==len(args)-1:
            end=i
            if i-args[index-1]!=1 and count<=1:
                new_array.extend([str(start),str(end)])
            else:
                new_array.append('-'.join([str(start),str(end)]))               
                
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
# print(solution([-69, -68, -65, -63, -61, -60, -58, -56, -53, -50, -47, -46, -45, -44, -43, -42, -41, -39, -36]))
# print(solution([-3,-2,-1,2,10,15,16,18,19,20]))#-3--1,2,10,15,16,18-20
# print(solution([-70, -67, -66, -65, -64, -62, -60, -57, -56, -54, -51, -49, -46, -44, -42, -40, -38, -36, -35, -32, -31, -30, -29, -26, -23, -20]))
#-70,-67--64,-62,-60,-57,-56,-54,-51,-49,-46,-44,-42,-40,-38,-36,-35,-32--29,-26,-23,-20
# print(solution([-87, -86, -85, -83, -82, -80, -78, -75, -73, -72, -69, -67, -66, -65, -62, -60, -58, -56, -54, -51, -48, -45, -43, -41, -39, -36]))
#-87--85,-83,-82,-80,-78,-75,-73,-72,-69,-67--65,-62,-60,-58,-56,-54,-51,-48,-45,-43,-41,-39,-36
#-87--85,-83,-82,-80,-78,-75,-73,-72,-69,-67--65,-62,-60,-58,-56,-54,-51,-48,-45,-43,-41,-39--36
print(solution([-54, -51, -48, -45, -42, -41, -40, -39, -37, -34, -31, -28, -27, -26, -24, -23, -21, -20, -19, -18, -16, -15, -12]))
#-54,-51,-48,-45,-42--39,-37,-34,-31,-28--26,-24,-23,-21--18,-16,-15,-12