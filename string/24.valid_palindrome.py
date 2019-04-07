"""
    LeetCode 680. Valid Palindrome II

    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

    Example 1:

    Input: "aba"
    Output: True
    Example 2:

    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.
    Note:

    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


def is_valid_palindrome(s):
    """
        :param s: Input string
        :return: True if valid palindrome, False otherwise
    """

    low = 0
    high = len(s) - 1
    mismatch_count = 0

    while low<high:
        print("heree", s[low], s[high], low, high)
        if s[low] == s[high]:
            low += 1
            high -= 1
        elif low+1 == high and mismatch_count < 1:
            return True
        elif s[low+1] == s[high]:
            low += 1
            mismatch_count += 1
        elif s[low] == s[high-1]:
            high -= 1
            mismatch_count += 1
        else:
            return False

        if mismatch_count > 1:
            return False
    return True



cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu