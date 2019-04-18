"""
    LeetCode 485. Max Consecutive Ones

    Given a binary array, find the maximum number of consecutive 1s in this array.

    Example 1:
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.
    Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""


def max_consecutive_ones(nums):
    """
        :param nums: Input array
        :return: Maximum consecutive ones
    """
    max = 0
    temp = 0
    for num in nums:
        if num == 1:
            temp += 1
        else:
            if temp > max:
                max = temp
            temp = 0
    return max if max > temp else temp
