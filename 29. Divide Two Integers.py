class Solution:
    def divide(self, dividend: int, divisor: int) -> int:  # noqa
        sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1
        ans = len(range(0, abs(dividend) - abs(divisor) + 1, abs(divisor)))
        ans = sign * ans
        return min(max(-(2 ** 31), ans), (2 ** 31 - 1))

        # failed attempt
        # def divide(self, dividend: int, divisor: int) -> int:  # noqa
        #     if abs(divisor) == 1:
        #         print(-2 ** 31)
        #         print(2 ** 31 - 1)
        #         if dividend < -2 ** 31:
        #             return - 2 ** 31
        #         elif abs(dividend) > 2 ** 31 - 1:
        #             return 2 ** 31 - 1
        #
        #     summation = 0
        #     count = 0
        #     if str(divisor)[0] == "-":
        #         if str(dividend)[0] == "-":
        #             return 1
        #             while summation >= dividend:
        #                 summation -= abs(divisor)
        #                 count += 1
        #             count -= 1
        #             return - count
        #         else:
        #             while summation <= dividend:
        #                 summation -= divisor
        #                 count += 1
        #             count -= 1
        #             return - count
        #     else:
        #         while summation <= dividend:
        #             summation += divisor
        #             count += 1
        #         return count - 1


if __name__ == '__main__':
    print(Solution().divide(-2147483648, -1))
