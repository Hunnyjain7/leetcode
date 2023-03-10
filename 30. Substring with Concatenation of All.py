from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:  # noqa
        words_len = len(words)
        word_len = len(words[0])
        s_len = len(s)
        substring_len = words_len * word_len
        if s_len < substring_len:
            return None  # noqa

        indexes = []
        i = 0
        while i <= (s_len - substring_len):
            all_in = True
            sub_string = s[i: i + substring_len]
            sub_strings = []

            for k in range(substring_len):
                if k % word_len == 0:
                    sub_strings.append(sub_string[k: k + word_len])

            for word in words:
                if word not in sub_strings:
                    all_in = False
                else:
                    sub_strings.remove(word)

            if all_in:
                indexes.append(i)
            i += 1
        return indexes


if __name__ == '__main__':
    print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
