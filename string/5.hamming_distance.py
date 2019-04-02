"""
    LeetCode 461. Hamming Distance

    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.

    Note:
    0 ≤ x, y < 231.

    Example:

    Input: x = 1, y = 4

    Output: 2

    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

    The above arrows point to positions where the corresponding bits are different.
"""


def hamming_distance(x, y):
    """

        :param x: First Integer
        :param y: Second Integer
        :return: Returns hamming distance between two integers
    """
    binary_x = list(map(lambda bit: int(bit), format(x, 'b')))
    binary_y = list(map(lambda bit: int(bit), format(y, 'b')))

    len_diff = abs(len(binary_y) - len(binary_x))

    count = 0

    if len(binary_x) < len(binary_y):
        temp_x = [0 for _ in range(0, len_diff)]
        temp_x.extend(binary_x)
        binary_x = temp_x
    else:
        temp_y = [0 for _ in range(0, len_diff)]
        temp_y.extend(binary_y)
        binary_y = temp_y

    for i in range(0, len(binary_x)):
        if binary_x[i] ^ binary_y[i]:
            count += 1
    return count


def hamming_distance(x, y):
    """
        :type x: int
        :type y: int
        :rtype: int
    """
    x = x ^ y
    y = 0
    while x:
        y += 1
        x = x & (x - 1)
    return y
