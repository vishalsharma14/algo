"""
    LeetCode 268. Missing Number

    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
    find the one that is missing from the array.

    Example 1:

    Input: [3,0,1]
    Output: 2
    Example 2:

    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8
    Note:
    Your algorithm should run in linear runtime complexity.
    Could you implement it using only constant extra space complexity?
"""


from collections import Counter


def find_missing_number(numbers):
    """
        :param numbers: Input array
        :return: Missing Number
    """
    num_dict = Counter(numbers)
    max_num = max(num_dict)

    for i in range(0, max_num + 1):
        if i not in num_dict:
            return i
    return max_num + 1
