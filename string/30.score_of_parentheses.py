"""
    LeetCode 856. Score of Parentheses

    Given a balanced parentheses string S, compute the score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.


    Example 1:

    Input: "()"
    Output: 1
    Example 2:

    Input: "(())"
    Output: 2
    Example 3:

    Input: "()()"
    Output: 2
    Example 4:

    Input: "(()(()))"
    Output: 6


    Note:

    S is a balanced parentheses string, containing only ( and ).
    2 <= S.length <= 50
"""


def score_of_parentheses(s):
    """
        :param s: Input String
        :return: Score Count
    """
    stack = []
    for ch in s:
        if ch == '(':
            stack.append("(")
        elif ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                if stack and type(stack[-1]) == int:
                    stack.append(1 + stack.pop())
                else:
                    stack.append(1)
            elif stack and type(stack[-1]) == int:
                num = stack.pop()
                stack.pop()
                if stack and type(stack[-1]) == int:
                    stack.append(2 * num + stack.pop())
                else:
                    stack.append(2 * num)
    return stack.pop()
