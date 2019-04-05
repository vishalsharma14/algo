"""
    443. String Compression

    Given an array of characters, compress it in-place.

    The length after compression must always be smaller than or equal to the original array.

    Every element of the array should be a character (not int) of length 1.

    After you are done modifying the input array in-place, return the new length of the array.


    Follow up:
    Could you solve it using only O(1) extra space?


    Example 1:

    Input:
    ["a","a","b","b","c","c","c"]

    Output:
    Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

    Explanation:
    "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


    Example 2:

    Input:
    ["a"]

    Output:
    Return 1, and the first 1 characters of the input array should be: ["a"]

    Explanation:
    Nothing is replaced.


    Example 3:

    Input:
    ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

    Output:
    Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

    Explanation:
    Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
    Notice each digit has it's own entry in the array.


    Note:

    All characters have an ASCII value in [35, 126].
    1 <= len(chars) <= 1000.
"""


# TODO: Update the input list in-place
def compress_list(char_list):
    """
        :param char_list: List of characters
        :return: Length of char list and compress list in place
    """
    count = 0
    char = char_list[0]
    output = []
    for c in char_list:
        if c != char:
            output.append(char)
            if count > 1:
                output.extend(list(str(count)))
            char = c
            count = 1
        else:
            count += 1
    output.append(char)
    if count > 1:
        output.extend(list(str(count)))
    for i in range(len(output)):
        char_list[i] = output[i]
    for _ in range(len(output), len(char_list)):
        char_list.pop()
    return len(char_list)
