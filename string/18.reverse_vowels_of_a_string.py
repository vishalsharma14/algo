"""
    LeetCode 345. Reverse Vowels of a String

    Write a function that takes a string as input and reverse only the vowels of a string.

    Example 1:

    Input: "hello"
    Output: "holle"
    Example 2:

    Input: "leetcode"
    Output: "leotcede"
    Note:
    The vowels does not include the letter "y".

"""


def reverse_vowels_of_a_string(str):
    """
        :param str: Input String
        :return: Reversed string
    """
    low = 0
    high = len(str) - 1
    vowels = ["a", "e", "i", "o", "u"]

    str_list = list(str)
    while low < high:
        if str_list[low].lower() not in vowels:
            low += 1
        elif str_list[high].lower() not in vowels:
            high -= 1
        else:
            str_list[low], str_list[high] = str_list[high], str_list[low]
            low += 1
            high -= 1
    return "".join(str_list)
