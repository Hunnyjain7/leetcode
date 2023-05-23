import string


class Solution:
    def numDecodings(self, s: str) -> int:  # noqa
        # cannot map to any character due to the leading zero
        if s[0] == '0':
            return 0
        n = len(s)
        # dp[i]: number of ways of decoding the substring s[:i]
        dp = [0 for _ in range(n + 1)]
        # base case
        dp[0] = 1
        for i in range(1, n + 1):
            # check single digit decode
            # valid decode is possible only when s[i - 1] is not zero
            # if so, take the previous state dp[i - 1]
            # e.g. AB - 1[2]
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            # check double digit decode
            # by looking at the previous two digits
            # if the substring belongs to the range [10 - 26]
            # then add the previous state dp[i - 2]
            # e.g. L - [12]
            if i >= 2:
                # or you can use `stoi(s.substr(i - 2, 2))`
                x = int(s[i - 2: i])
                # check the range
                if 10 <= x <= 26:
                    dp[i] += dp[i - 2]
        return dp[n]

    def numDecodings3(self, s: str) -> int:  # noqa
        s_len = len(s)
        hashmap = {f"{i + 1}": string.ascii_uppercase[i] for i in range(26)}
        visited = set()

        def decode(st):
            new = ""
            for i in st:
                if i == "0":
                    return
                new += hashmap[i]
            return new

        decoded_s = decode(s)
        if decoded_s:
            visited.add(decoded_s)

        for i in range(s_len):
            j = i + 1
            if s[i] in ["1", "2"] and j < s_len and s[j] in ["0", "1", "2", "3", "4", "5", "6"]:
                decoded_si = decode(s[:i])
                decoded_sj = decode(s[j + 1:])
                if decoded_si is None or decoded_sj is None:
                    continue
                visited.add(decoded_si + hashmap[s[i:j + 1]] + decoded_sj)
                curr = set()
                for visit in visited:
                    curr.add(visit[:i] + hashmap[s[i:j + 1]] + visit[j + 1:])
                visited.update(curr)

        return len(visited)

    def numDecodings2(self, s: str) -> int:  # noqa
        s_len = len(s)
        res = 0

        def recursion(i, curr):
            nonlocal res
            if i >= s_len or s[i] == "0":
                print(curr)
                return res
            if s[i] in ["1", "2"] and (i + 1) < s_len and s[i + 1] in ["1", "2", "3", "4", "5", "6"]:
                print(s[i])
                print(s[i] + s[i + 1])
                recursion(i + 1, curr)
            return res

        return recursion(0, "")


if __name__ == '__main__':
    print(Solution().numDecodings("12451789315499"))
