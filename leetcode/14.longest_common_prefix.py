"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        first_str = list(strs[0])
        count = 0
        for i in range(len(first_str)):
            ch = first_str[i]
            match = True
            for j in range(1, len(strs)):
                string = list(strs[j])
                if i > len(string) - 1:
                    return "".join(first_str[:count])
                if ch != string[i]:
                    match = False
                    return "".join(first_str[:count])
            if match:
                count += 1
        return "".join(first_str[:count])
