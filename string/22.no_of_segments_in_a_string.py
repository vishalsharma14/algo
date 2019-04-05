"""
    LeetCode 434. Number of Segments in a String

    Count the number of segments in a string, where a segment is defined to be a
    contiguous sequence of non-space characters.

    Please note that the string does not contain any non-printable characters.

    Example:

    Input: "Hello, my name is John"
    Output: 5
"""

def no_of_segments_in_a_string(input_string):
    """
        :param input_string: Input string
        :return: Number of segments separated by a space
    """
    # input_string = input_string.strip()
    # if len(input_string) == 0:
    #     return 0
    # string.split() handles extra spaces by itself
    return len(input_string.split())
