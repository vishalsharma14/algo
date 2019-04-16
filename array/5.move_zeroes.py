"""
    LeetCode 283. Move Zeroes

    Given an array nums, write a function to move all 0's to the end of it
    while maintaining the relative order of the non-zero elements.

    Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""


def move_zeroes(arr):
    """
        :param arr: Input Array
        :return: Array after moving zeroes at the end
    """
    zero_count = 0
    length = len(arr)
    i = 0
    while i < length:
        if arr[i] == 0:
            arr.pop(i)
            length -= 1
            i -= 1
            zero_count += 1
        i += 1
    for _ in range(zero_count):
        arr.append(0)
