"""
    LeetCode 551. Student Attendance Record I


    You are given a string representing an attendance record for a student.
    The record only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
    A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent)
    or more than two continuous 'L' (late).

    You need to return whether the student could be rewarded according to his attendance record.

    Example 1:

    Input: "PPALLP"
    Output: True
    Example 2:

    Input: "PPALLL"
    Output: False
"""


import re


def can_student_get_reward(attendance):
    """
        :param attendance: Attendance string
        :return: True if student can be rewarded, False otherwise
    """

    if len(re.findall("[A]", attendance)) > 1 or "LLL" in attendance:
        return False
    return True
