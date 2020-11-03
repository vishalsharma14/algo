"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function
returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1

"""

class Solution:
    def reverse(self, x: int) -> int:
        """
            :param x: Input integer
            :return: Reversed Integer if in range, 0 otherwise
        """
        if x < 0:
            response = f"-{str(x)[:0:-1]}"
        else:
            response = str(x)[::-1]
        response = int(response)

        max_num = 2147483648 # 2**31

        if response not in range(-max_num, max_num):
            return 0
        return response
