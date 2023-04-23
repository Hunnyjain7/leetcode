class Solution:
    def lengthOfLastWord(self, s: str) -> int:  # noqa
        return len(s.strip().split(" ")[-1])


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
