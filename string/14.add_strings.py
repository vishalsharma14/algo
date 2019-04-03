"""
    LeetCode 415. Add Strings

    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

    Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def add_strings(num1, num2):
    """
        :param num1: Number 1 as string
        :param num2: Number 2 as string
        :return: Sum of num1 and num2 - String
    """
    ptr1 = len(num1) - 1
    ptr2 = len(num2) - 1
    sum = ""
    offset = 0

    while ptr1 >= 0 and ptr2 >= 0:
        temp = int(num1[ptr1]) + int(num2[ptr2]) + offset
        sum += str(int(temp%10))
        offset = int(temp/10)
        ptr1 -= 1
        ptr2 -= 1

    while ptr1 >= 0:
        temp = int(num1[ptr1]) + offset
        sum += str(int(temp%10))
        offset = int(temp/10)
        ptr1 -= 1

    while ptr2 >= 0:
        temp = int(num2[ptr2]) + offset
        sum += str(int(temp%10))
        offset = int(temp/10)
        ptr2 -= 1

    if offset > 0:
        sum += str(offset)

    return sum[::-1]
