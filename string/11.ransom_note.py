"""
    LeetCode 383. Ransom Note

    Given an arbitrary ransom note string and another string containing letters
    from all the magazines, write a function that will return true if the ransom note
    can be constructed from the magazines ; otherwise, it will return false.

    Each letter in the magazine string can only be used once in your ransom note.

    Note:
    You may assume that both strings contain only lowercase letters.

    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""


def can_construct_ransom_note(ransom_string, magazine_string):
    """
    :param ransom_string: Ransom Note String
    :param magazine_string: String containing letters from all the magazines
    :return:
        True if ransom note can be constructed
        False if ransom note cannot be constructed
    """
    ransom_dict = {}
    for char in ransom_string:
        if ransom_dict.get(char):
            ransom_dict[char] += 1
        else:
            ransom_dict[char] = 1

    magazine_dict = {}
    for char in magazine_string:
        if magazine_dict.get(char):
            magazine_dict[char] += 1
        else:
            magazine_dict[char] = 1

    for key in ransom_dict.keys():
        if not (magazine_dict.get(key) and ransom_dict[key] <= magazine_dict[key]):
            return False
    return True
