"""
    LeetCode 890. Find and Replace Pattern

    You have a list of words and a pattern, and you want to know which words in words matches the pattern.

    A word matches the pattern if there exists a permutation of letters p so that after
    replacing every letter x in the pattern with p(x), we get the desired word.

    (Recall that a permutation of letters is a bijection from letters to letters: every letter
    maps to another letter, and no two letters map to the same letter.)

    Return a list of the words in words that match the given pattern.

    You may return the answer in any order.



    Example 1:

    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
    "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
    since a and b map to the same letter.


    Note:

    1 <= words.length <= 50
    1 <= pattern.length = words[i].length <= 20
"""


def find_and_replace(words, pattern):
    """
        :param words: List of words
        :param pattern: Pattern string
        :return: List of words matching the patten
    """

    def match(word):
        """
            :param word:
            :return: True if the word matches the pattern, False otherwise
        """
        permutation = {}
        for x, y in zip(word, pattern):
            if permutation.setdefault(x, y) != y:
                return False
        return len(permutation.values()) == len(set(permutation.values()))

    return list(filter(match, words))