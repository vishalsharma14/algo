"""
    LeetCode 66. Plus One

    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

    The digits are stored such that the most significant digit is at the head of the list,
    and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.

    Example 1:

    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Example 2:

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
"""


def plus_one(arr):
    """
        :param arr: Input Array
        :return: Array after adding 1 to the integer representation
    """
    n = len(arr)
    output = []

    int_num = 0
    for i in range(n):
        int_num += arr[i] * pow(10, n-1-i)

    int_num += 1

    while int_num > 0:
        remaining, remainder = divmod(int_num, 10)
        output.insert(0, remainder)
        int_num = remaining
    return output