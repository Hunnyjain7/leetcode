"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:  # noqa
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        s_len = len(s)
        start = 0
        end = s_len - 1
        while start < end:
            while s[start] not in vowels and start < end:
                start += 1
            while s[end] not in vowels and start < end:
                end -= 1
            if start < end:
                s = s[:start] + s[end] + s[start + 1:end] + s[start] + s[end + 1:]
            start += 1
            end -= 1
        return s


if __name__ == '__main__':
    print(Solution().reverseVowels("hello"))
