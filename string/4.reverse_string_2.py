"""
    LeetCode 541. Reverse String II

    Given a string and an integer k, you need to reverse the first k characters for every
    2k characters counting from the start of the string. If there are less than k characters
    left, reverse all of them. If there are less than 2k but greater than or equal to k characters,
    then reverse the first k characters and left the other as original.

    Example:

    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"
    Restrictions:
    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]
"""


def reverse_string(input_string, k):
    length = len(input_string)
    pointer = 0
    response = ""
    while pointer + 2 * k < length:
        sub_str = input_string[pointer:pointer + 2*k]
        response += sub_str[k-1::-1] + sub_str[k:]

        pointer += 2*k

    sub_str = input_string[pointer:]
    if len(sub_str) < k:
        response += sub_str[::-1]
    else:
        response += sub_str[k - 1::-1] + sub_str[k:]
    return response
