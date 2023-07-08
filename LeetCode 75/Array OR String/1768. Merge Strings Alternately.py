"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end of
the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:  # noqa
        word1_len = len(word1)
        word2_len = len(word2)
        i = 0
        curr = ""

        def merge():
            nonlocal curr, i
            if i >= word1_len or i >= word2_len:
                return
            curr += word1[i] + word2[i]
            i += 1
            merge()

        merge()
        if i == word1_len and i == word2_len:
            return curr
        elif i < word2_len:
            return curr + word2[i:]
        else:
            return curr + word1[i:]


if __name__ == '__main__':
    print(Solution().mergeAlternately("abc", "pqr"))
