class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:  # noqa
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len:
            return False

        dp = {}

        def dfs(i, j):
            if i == s1_len and j == s2_len:
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            if i < s1_len and s3[i + j] == s1[i] and dfs(i + 1, j):
                return True

            if j < s2_len and s3[i + j] == s2[j] and dfs(i, j + 1):
                return True

            dp[(i, j)] = False

        return dfs(0, 0)


if __name__ == '__main__':
    print(Solution().isInterleave("aadbcc", "dbbca", "aadbbcdbcac"))
