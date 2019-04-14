"""
    LeetCode 922. Sort Array By Parity II

    Given an array A of non-negative integers, half of the integers in A are odd,
    and half of the integers are even.

    Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

    You may return any answer array that satisfies this condition.



    Example 1:

    Input: [4,2,5,7]
    Output: [4,5,2,7]
    Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


    Note:

    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000
"""


def sort_array(a):
    """
        :param a: Input Array
        :return: Sorted Array
    """
    output = []
    even_index = 0
    odd_index = 1
    for ele in a:
        if ele % 2 == 0:
            output.insert(even_index, ele)
            even_index += 2
        else:
            output.insert(odd_index, ele)
            odd_index += 2
    return output


def sort_array_second(a):
    """
        :param a: Input Array
        :return: Sorted Array
    """
    even_index = 0
    odd_index = 1
    size = len(a)

    while even_index < size and odd_index < size:
        if a[even_index] % 2 == 0:
            even_index += 2
        elif a[odd_index] % 2 == 1:
            odd_index += 2
        else:
            a[even_index], a[odd_index] = a[odd_index], a[even_index]
            even_index += 2
            odd_index += 2
    return a
