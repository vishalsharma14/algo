"""
    LeetCode 67. Add Binary

    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.

    Example 1:

    Input: a = "11", b = "1"
    Output: "100"
    Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"
"""


def add_binary(str1, str2):
    """
        :param str1:  Binary String 1
        :param str2: Binary String 1
        :return: Sum of Binary strings
    """
    carry = "0"
    sum = ""

    len_diff = abs(len(str1) - len(str2))
    if len(str1) <= len(str2):
        str1 = "0" * len_diff + str1
    else:
        str2 = "0" * len_diff + str2

    for i in range(len(str1) - 1, -1, -1):
        temp_str = carry + str1[i] + str2[i]
        if temp_str == "000":
            sum = "0" + sum
            carry = "0"
        elif temp_str in ["001", "010", "100"]:
            sum = "1" + sum
            carry = "0"
        elif temp_str in ["011", "101", "110"]:
            sum = "0" + sum
            carry = "1"
        elif temp_str == "111":
            sum = "1" + sum
            carry = "1"
    if carry == "1":
        sum = carry + sum
    return sum
