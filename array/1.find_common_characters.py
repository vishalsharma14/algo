"""
    LeetCode 1002. Find Common Characters

    Given an array A of strings made only from lowercase letters, return a list of all
    characters that show up in all strings within the list (including duplicates).
    For example, if a character occurs 3 times in all strings but not 4 times,
    you need to include that character three times in the final answer.

    You may return the answer in any order.



    Example 1:

    Input: ["bella","label","roller"]
    Output: ["e","l","l"]
    Example 2:

    Input: ["cool","lock","cook"]
    Output: ["c","o"]


    Note:

    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] is a lowercase letter
"""


from collections import Counter

def common_characters(a):
    """
        :param a: List of strings
        :return: List of Common characters
    """
    common_char_list = list(a[0])

    length = len(common_char_list)
    for i in range(1, len(a)):
        char_count_dict = Counter(a[i])
        j = 0
        while j < length:
            ch = common_char_list[j]
            if char_count_dict.get(ch, 0) < 1:
                common_char_list.pop(j)
                length -= 1
                j -= 1
            else:
                char_count_dict[ch] -= 1
            j += 1
    return common_char_list

