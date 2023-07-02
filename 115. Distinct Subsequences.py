class Solution:
    def numDistinct(self, s: str, t: str) -> int:  # noqa
        s_len = len(s)
        t_len = len(t)
        if s_len < t_len:
            return 0

        prev = [0] * (s_len + 1)
        prev[0] = 1
        for i in range(1, s_len + 1):
            curr = [0] * (t_len + 1)
            curr[0] = 1
            for j in range(1, t_len + 1):
                x = 0
                if s[i - 1] == t[j - 1]:
                    x = prev[j - 1]
                curr[j] = prev[j] + x
            prev = curr
        return prev[-1]

    def numDistinctWithMemoization(self, s: str, t: str) -> int:  # noqa
        n = len(s)
        m = len(t)
        if n < m:
            return 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                x = 0
                if s[i - 1] == t[j - 1]:
                    x = dp[i - 1][j - 1]
                y = dp[i - 1][j]
                dp[i][j] = x + y
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().numDistinct("rabbbit", "rabbit"))
