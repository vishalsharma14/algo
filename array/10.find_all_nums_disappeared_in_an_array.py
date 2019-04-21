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
