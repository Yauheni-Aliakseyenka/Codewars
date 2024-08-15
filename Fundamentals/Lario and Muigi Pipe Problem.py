'''
Given a list of unique numbers sorted in ascending order, return a new list so that the values increment
by 1 for each index from the minimum value up to the maximum value (both included).
'''


def pipe_fix(nums):
    return [i for i in range(nums[0], nums[-1] + 1)]


def pipe_fix1(nums):
    return list(range(nums[0], nums[-1] + 1))

