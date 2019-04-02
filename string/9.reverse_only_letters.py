"""
    LeetCode 917. Reverse Only Letter

    Given a string S, return the "reversed" string where all characters that are
    not a letter stay in the same place, and all letters reverse their positions.



    Example 1:

    Input: "ab-cd"
    Output: "dc-ba"
    Example 2:

    Input: "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"
    Example 3:

    Input: "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"


    Note:

    S.length <= 100
    33 <= S[i].ASCIIcode <= 122
    S doesn't contain \ or "
"""


def reverse_only_letters(S):
    """
        :param S: Input String
        :return: Updated reversed string
    """
    lower = 0
    high = len(S) - 1
    char_list = list(S)
    while lower < high:
        if not (97 <= ord(char_list[lower]) <= 122 or 65 <= ord(char_list[lower]) <= 90):
            lower += 1
        elif not (97 <= ord(char_list[high]) <= 122 or 65 <= ord(char_list[high]) <= 90):
            high -= 1
        else:
            char_list[lower], char_list[high] = char_list[high], char_list[lower]
            lower += 1
            high -= 1
    return "".join(char_list)


