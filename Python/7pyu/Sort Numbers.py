"https://www.codewars.com/kata/5174a4c0f2769dd8b1000003"


def solution(nums: list):
    if not nums:
        return []
    nums.sort()
    return nums


print(solution([3, 6, 4, 5, 2, 2, 4, 0]))
