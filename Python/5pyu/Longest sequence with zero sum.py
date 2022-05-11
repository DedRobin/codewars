#https://www.codewars.com/kata/52b4d1be990d6a2dac0002ab

def max_zero_sequence(arr):
    longest_zero_sum=[]
    for start in range(len(arr)):
        for end in range(1,len(arr)):        
            if not sum(arr[start:end]):
                if len(longest_zero_sum)<len(arr[start:end]):
                    longest_zero_sum=arr[start:end]
    return longest_zero_sum