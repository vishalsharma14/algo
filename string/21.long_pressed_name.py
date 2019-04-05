"""
    LeetCode 925. Long Pressed Name

    Your friend is typing his name into a keyboard.  Sometimes, when typing a character c,
    the key might get long pressed, and the character will be typed 1 or more times.

    You examine the typed characters of the keyboard.  Return True if it is possible that
    it was your friends name, with some characters (possibly none) being long pressed.



    Example 1:

    Input: name = "alex", typed = "aaleex"
    Output: true
    Explanation: 'a' and 'e' in 'alex' were long pressed.
    Example 2:

    Input: name = "saeed", typed = "ssaaedd"
    Output: false
    Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
    Example 3:

    Input: name = "leelee", typed = "lleeelee"
    Output: true
    Example 4:

    Input: name = "laiden", typed = "laiden"
    Output: true
    Explanation: It's not necessary to long press any character.


    Note:

    name.length <= 1000
    typed.length <= 1000
    The characters of name and typed are lowercase letters.
"""


def long_pressed_name(name, typed):
    """
        :param name: Input name string
        :param typed: Typed string
        :return:
            True: If name was lon pressed
            False: Otherwise
    """
    ptr1 = 0
    ptr2 = 0
    prev_char = name[0]
    while ptr1 < len(name) and ptr2 < len(typed):
        if name[ptr1] == typed[ptr2]:
            prev_char = name[ptr1]
            ptr1 += 1
            ptr2 += 1
        elif typed[ptr2] == prev_char:
            ptr2 += 1
        else:
            return False
    if ptr1 < len(name):
        return False
    return True
