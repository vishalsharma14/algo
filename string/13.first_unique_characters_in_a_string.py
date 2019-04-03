"""
    LeetCode 387. First Unique Character in a String


    Given a string, find the first non-repeating character in it and return it's index.
    If it doesn't exist, return -1.

    Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.
    Note: You may assume the string contain only lowercase letters.


"""

from collections import Counter


def index_of_first_unique_character(s):
    """
        :param s: Input string
        :return: Index of first unique character or -1
    """
    char_dict = Counter(s)
    for i in range(len(s)):
        if char_dict[s[i]] == 1:
            return i
    return -1
