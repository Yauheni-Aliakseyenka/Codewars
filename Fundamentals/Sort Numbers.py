'''
Finish the solution so that it sorts the passed in array of numbers.
If the function passes in an empty array or null/nil value then it should return an empty array.
'''


def solution(nums):
    return [] if nums is None else sorted(nums)


def solution1(nums):
    return sorted(nums) if nums else []


def solution2(nums):
    return sorted(nums or [])