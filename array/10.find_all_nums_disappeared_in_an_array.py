"""
    LeetCode 448. Find All Numbers Disappeared in an Array

    Given an array of integers where 1 <= a[i] <= n (n = size of array),
    some elements appear twice and others appear once.

    Find all the elements of [1, n] inclusive that do not appear in this array.

    Could you do it without extra space and in O(n) runtime?
    You may assume the returned list does not count as extra space.

    Example:

    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]
"""


from collections import Counter


def find_disappeared_nums(nums):
    """
        :param nums: Input Array
        :return: Array of disappeared numbers
    """
    n = len(nums)
    num_dict = Counter(nums)
    output = []

    for i in range(1, n+1):
        if i not in num_dict:
            output.append(i)
    return output


def find_disappeared_nums_second(nums):
    """
        :param nums: Input Array
        :return: Array of disappeared numbers
    """
    n = len(nums)
    num_dict = {}

    for i in range(1, n+1):
        num_dict[i] = 1

    for num in nums:
        if num in num_dict:
            del num_dict[num]

    return num_dict.keys()


def find_disappeared_nums_third(nums):
    """
        :param nums: Input Array
        :return: Array of disappeared numbers
    """
    result = []

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    print(nums)

    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
    return result
