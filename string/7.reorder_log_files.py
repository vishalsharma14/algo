"""
    LeetCode 937. Reorder Log Files

    You have an array of logs.  Each log is a space delimited string of words.

    For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.
    We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed
    that each log has at least one word after its identifier.

    Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs
    are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
    The digit-logs should be put in their original order.

    Return the final order of the logs.



    Example 1:

    Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


    Note:

    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""


def reorder_log_files(logs):
    """
    :param logs: List of logs
    :return: Ordered Logs
    """

    letter_logs = []
    digit_logs = []
    letter_logs_dict = {}
    for log in logs:
        first_char = log.split(" ")[1][0]
        # Letter Log
        if 97 <= ord(first_char) <= 122:
            letter_logs_dict[" ".join(log.split(" ")[1:])] = log
        else:
            digit_logs.append(log)

    for key in sorted(letter_logs_dict.keys()):
        letter_logs.append(letter_logs_dict[key])

    letter_logs.extend(digit_logs)

    return letter_logs
