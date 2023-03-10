class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  # noqa
        ret = -1
        if needle not in haystack:
            return ret

        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return ret


if __name__ == '__main__':
    print(Solution().strStr("sadbutsad", "sad"))
