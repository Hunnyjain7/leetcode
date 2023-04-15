class Solution:
    # Copied
    def isMatch(self, s: str, p: str) -> bool:  # noqa
        s, p = "#" + s, "#" + p  # for the cases where p starts with *
        s_len = len(s)
        p_len = len(p)
        dp = [[False for _ in range(p_len + 1)] for _ in range(s_len + 1)]
        dp[0][0] = True

        for r in range(1, s_len + 1):
            for c in range(1, p_len + 1):
                if p[c - 1] == "*":
                    dp[r][c] = dp[r - 1][c] or dp[r][c - 1]
                elif p[c - 1] == "?" or p[c - 1] == s[r - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
        return dp[-1][-1]

    # My Approach Failed
    def isMatch2(self, s: str, p: str) -> bool:  # noqa
        its_star = False
        new = ""
        skipper = ""
        if "*" not in p:
            if len(s) != len(p):
                return False
        for i in range(len(s)):
            if i >= len(p) and not its_star:
                return False
            if its_star:
                if not skipper:
                    new += s[i]
                elif skipper[0] == s[i]:
                    its_star = False
                    new += skipper[1:] + s[i]
                    skipper = ""
                else:
                    skipper += s[i]
                # new += s[i]
            elif p[i] == s[i]:
                new += s[i]
            elif p[i] == "*":
                its_star = True
                if i + 1 >= len(p):
                    new += s[i]
                    continue
                skipper = p[i + 1]
                if skipper == s[i]:
                    its_star = False
                    skipper = ""
                    p = p[1:]
                new += s[i]

            elif p[i] == "?":
                new += s[i]
            else:
                return False
        print(new)
        return True if s == new else False


if __name__ == '__main__':
    # print(Solution().isMatch("acdcb", "a*c?b"))
    print(Solution().isMatch("adceb", "*a*b"))
    # print(Solution().isMatch("aa", "*"))
    # print(Solution().isMatch("abcabczzzde", "*abc???de*"))
    # print(Solution().isMatch("a", "aa"))
