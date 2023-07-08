"""For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters."""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:  # noqa
        for i in range(len(str2), 0, -1):
            s1 = str1
            s2 = str2
            s = str2[:i]
            s1 = s1.replace(s, "")
            s2 = s2.replace(s, "")
            if not s1 and not s2:
                return s
        return ""


if __name__ == '__main__':
    print(Solution().gcdOfStrings("ABABAB", "ABAB"))
