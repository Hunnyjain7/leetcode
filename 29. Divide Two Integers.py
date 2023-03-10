class Solution:
    def divide(self, dividend: int, divisor: int) -> int:  # noqa
        if abs(divisor) == 1:
            print(-2 ** 31)
            print(2 ** 31 - 1)
            if dividend < -2 ** 31:
                return - 2 ** 31
            elif abs(dividend) > 2 ** 31 - 1:
                return 2 ** 31 - 1

        summation = 0
        count = 0
        if str(divisor)[0] == "-":
            if str(dividend)[0] == "-":
                return 1
                while summation >= dividend:
                    summation -= abs(divisor)
                    count += 1
                count -= 1
                return - count
            else:
                while summation <= dividend:
                    summation -= divisor
                    count += 1
                count -= 1
                return - count
        else:
            while summation <= dividend:
                summation += divisor
                count += 1
            return count - 1


if __name__ == '__main__':
    print(Solution().divide(-2147483648, -1))
    print(2 ** 31)
