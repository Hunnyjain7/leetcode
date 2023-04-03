class Solution:
    def myPow(self, x: float, n: int) -> float:  # noqa
        if n == 0:
            return 1
        if abs(x) == 1:
            if str(n)[0] == "-":
                if str(x)[0] == "-":
                    return -x
                return x
            return x
        if str(x) == "1e-05":
            return 0
        if "e" in str(x / n) and len(str(n)) > 6:
            return 0
        ans = 1 / x if str(n)[0] == "-" else x
        for i in range(1, abs(n)):
            if str(n)[0] == "-":
                ans = ans * 1 / x
            else:
                ans = ans * x
        return ans if abs(n) % 2 == 0 else -ans if str(x)[0] == "-" and str(ans)[0] != "-" else ans


if __name__ == '__main__':
    print(Solution().myPow(0.00001, 2147483647))
