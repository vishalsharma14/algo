"""
    LeetCode 557. Reverse Words in a String III

    Given a string, you need to reverse the order of characters in each word within a sentence
    while still preserving whitespace and initial word order.

    Example 1:

    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    Note: In the string, each word is separated by single space and there will not be any
    extra space in the string.
"""


def reverse_word_in_a_string(S):
    """

    :param S:
    :return:
    """
    output = []
    for word in S.split(" "):
        output.append(word[::-1])
    return " ".join(output)