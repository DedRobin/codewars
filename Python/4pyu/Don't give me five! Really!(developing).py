"""
This kata is the performance version of Don't give me five by user5036852.

Your mission, should you accept it, is to return the count of all integers in a given range which do not contain the digit 5 (in base 10 representation).
You are given the start and the end of the integer range. The start and the end are both inclusive.

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> return 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> return 12
The result may contain fives. ;-)
The start will always be smaller than the end. Both numbers can be also negative.

The regions can be very large and there will be a large number of test cases. So brute force solutions will certainly time out!

Good luck, warrior!
"""
import os
os.system('cls||clear')

def dont_give_me_five(start, end):
    if start<0:
        if end<0:
            count=abs(start)-abs(end)+1
        else:
            count=abs(start)+abs(end)+1
    elif start==0:
        count=end
    elif end==0:
        count=abs(start)
    else:
        count=end-start+1
    print(f'[{start} - {end}]','\nCount =',count)
    number_of_diviver_on_five=count//10
    a=start%10
    if 0<=start<=4 or (start<0 and 6<=abs(start)%10<=9):
        number_of_diviver_on_five+=1
    return count-number_of_diviver_on_five

print(dont_give_me_five(-17, 9))#24
print(dont_give_me_five(1, 9))#8
print(dont_give_me_five(4, 17))#12
print(dont_give_me_five(-17, -4))#12

print(dont_give_me_five(0, 500))#326131553237897713
