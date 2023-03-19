class Solution:
    def countAndSay(self, n: int) -> str:  # noqa
        dp = "1"
        for i in range(1, n):
            count = 0
            prev = ""
            rem = False
            bhar = False
            temp = ""
            for j in dp:
                if rem:
                    rem = False
                if not prev or j == prev:
                    prev = j
                    count += 1
                else:
                    temp += str(count) + prev
                    prev = j
                    rem = True
                    bhar = True
                    count = 1
            if bhar:
                temp += str(count) + prev
                dp = temp
            elif temp:
                dp = str(count) + temp
            else:
                dp = str(count) + prev
        return dp


if __name__ == '__main__':
    print(Solution().countAndSay(8))
# i:9 dp[8]:1113213211
# i:8 dp[7]:13112221
# i:7 dp[6]:312211
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
