"""
    LeetCode 686. Repeated String Match

    Given two strings A and B, find the minimum number of times A has to be repeated
    such that B is a substring of it. If no such solution, return -1.

    For example, with A = "abcd" and B = "cdabcdab".

    Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it;
    and B is not a substring of A repeated two times ("abcdabcd").

    Note:
    The length of A and B will be between 1 and 10000.
"""


def repeated_string_match(a, b):
    """
        :param a: Input string A
        :param b: Input string B
        :return: Number of times A should be repeated so that B is a substring of A
    """
    multiplier = (len(b) -1) // len(a) + 1
    for i in range(2):
        if b in a * (multiplier + i):
            return multiplier + i
    return -1
