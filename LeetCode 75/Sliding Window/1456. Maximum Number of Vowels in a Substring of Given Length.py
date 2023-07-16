"""Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:  # noqa
        vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        for n in s[:k]:
            if n in vowels:
                vowels[n] += 1
        count = sum(vowels.values())
        prev = s[0]
        for i in range(k, len(s)):
            if prev in vowels:
                vowels[prev] -= 1
            if s[i] in vowels:
                vowels[s[i]] += 1
            count = max(count, sum(vowels.values()))
            prev = s[i - k + 1]
        return count


if __name__ == '__main__':
    print(Solution().maxVowels("leetcode", 3))
