"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false


Constraints:

-231 <= x <= 231 - 1


"""

# Converting str to int
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            :param x: Input integer
            :reutrn: True if number is palindrome
                False if number is not a palindrome
        """
        if x < 0:
            return False
        if str(x)[::-1] == str(x):
            return True
        return False

# Using division
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            :param x: Input integer
            :reutrn: True if number is palindrome
                False if number is not a palindrome
        """
        if x < 0:
            return False
        temp = x
        reverse = 0
        while temp != 0:
            reverse =  reverse * 10 + (temp % 10)
            temp = int(temp/10)
        return reverse == x
