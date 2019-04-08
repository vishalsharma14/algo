"""
    LeetCode 20. Valid Parentheses

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    Example 1:

    Input: "()"
    Output: true
    Example 2:

    Input: "()[]{}"
    Output: true
    Example 3:

    Input: "(]"
    Output: false
    Example 4:

    Input: "([)]"
    Output: false
    Example 5:

    Input: "{[]}"
    Output: true
"""


def does_string_has_valid_parenthesis(s):
    """
        :param s: Input String
        :return: True if string has valid parenthesis, False otherwise
    """
    brackets_pair = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    stack = []
    if len(s) == 0:
        return True
    for ch in s:
        if brackets_pair.get(ch) and len(stack) > 0 and brackets_pair[ch] == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    if len(stack) == 0:
        return True
    return False
