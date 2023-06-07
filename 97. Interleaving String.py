class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:  # noqa
        # True means s1 and False means s2
        s = True
        s1_idx, s2_idx, s3_idx = 0, 0, 0
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        while s1_idx < s1_len and s2_idx < s2_len and s3_idx < s3_len:
            if s:
                pass
            else:
                pass
        return s


if __name__ == '__main__':
    print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
