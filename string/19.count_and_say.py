"""
    LeetCode 38. Count and Say

    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 <= n <= 30, generate the nth term of the count-and-say sequence.

    Note: Each term of the sequence of integers will be represented as a string.
"""


def count_and_say(n):
    """
        :param n: Input Integer
        :return: nth term of the count-and-say sequence
    """
    num_list = ["1"]

    for _ in range(2, n+1):
        last_num = num_list[-1]
        new_num_stack = []
        new_num = ""
        for i in range(len(last_num)):
            if len(new_num_stack) == 0 or last_num[i] == new_num_stack[-1]:
                new_num_stack.append(last_num[i])
            else:
                new_num += str(len(new_num_stack)) + new_num_stack.pop()
                new_num_stack = list()
                new_num_stack.append(last_num[i])

        if len(new_num_stack) != 0:
            new_num += str(len(new_num_stack)) + new_num_stack.pop()
        num_list.append(new_num)
    return num_list[n-1]
