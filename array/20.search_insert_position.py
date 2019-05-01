"""
    LeetCode 35. Search Insert Position

    Given a sorted array and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Example 1:

    Input: [1,3,5,6], 5
    Output: 2
    Example 2:

    Input: [1,3,5,6], 2
    Output: 1
    Example 3:

    Input: [1,3,5,6], 7
    Output: 4
    Example 4:

    Input: [1,3,5,6], 0
    Output: 0
"""


def get_insert_position(array, target):
    """
        :param array: Input array
        :param target: Target Value
        :return: Index where target is found or should be inserted
    """
    for i in range(len(array)):
        if array[i] > target:
            return i
        elif array[i] == target:
            return i
    return len(array)


def get_insert_position_second(array, target):
    """
        :param array: Input array
        :param target: Target Value
        :return: Index where target is found or should be inserted
    """
    for i in range(len(array)):
        if array[i] >= target:
            return i
    return len(array)
