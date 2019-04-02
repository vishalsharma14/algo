"""
    LeetCode 788. Rotated Digits

    X is a good number if after rotating each digit individually by 180 degrees,
    we get a valid number that is different from X.  Each digit must be rotated -
    we cannot choose to leave it alone.

    A number is valid if each digit remains a digit after rotation. 0, 1, and 8
    rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other,
    and the rest of the numbers do not rotate to any other number and become invalid.

    Now given a positive number N, how many numbers X from 1 to N are good?

    Example:
    Input: 10
    Output: 4
    Explanation:
    There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
    Note:

    N  will be in range [1, 10000].
"""


def rotated_digits(N):
    """
        :param N: Integer Input
        :return: Count of good numbers
    """
    good_numbers = [0, 1, 8, 2, 5, 6, 9]
    self_rotating_numbers = [0, 1, 8]
    count = 0

    for i in range(1, N+1):
        num = i
        digits = []
        while num > 0:
            temp = int(num % 10)
            digits.append(temp)
            num = int(num / 10)
        if len(set(digits).intersection(self_rotating_numbers)) != len(set(digits)) and \
                len(set(digits).intersection(good_numbers)) == len(set(digits)):
            count += 1
    return count


def rotated_digits_second_method(N):
    """
        :param N: Integer Input
        :return: Count of good numbers
    """
    good_numbers = ["0", "1", "8", "2", "5", "6", "9"]
    self_rotating_numbers = ["0", "1", "8"]
    count = 0

    for i in range(1, N+1):
        number_set = set(str(i))

        if len(number_set.intersection(self_rotating_numbers)) != len(number_set) and \
                len(number_set.intersection(good_numbers)) == len(number_set):
            count += 1
    return count
