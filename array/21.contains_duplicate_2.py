"""
    LeetCode 219. Contains Duplicate II

    Given an array of integers and an integer k, find out whether there are
    two distinct indices i and j in the array such that nums[i] = nums[j]
    and the absolute difference between i and j is at most k.

    Example 1:

    Input: nums = [1,2,3,1], k = 3
    Output: true
    Example 2:

    Input: nums = [1,0,1,1], k = 1
    Output: true
    Example 3:

    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
"""


def contains_duplicate(nums, k):
    """
        :param nums: Input Array
        :param k: Integer to check duplicates in range
        :return: True if duplicate exists, False otherwise
    """

    num_dict = {}

    for i in range(len(nums)):
        if nums[i] not in num_dict:
            num_dict[nums[i]] = [i]
        elif i - num_dict[nums[i]][-1] <= k:
            return True
        else:
            num_dict[nums[i]].append(i)

    return False