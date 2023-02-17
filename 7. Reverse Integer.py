class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_reverse = -int(str(x)[:0:-1]) if str(x)[0] == "-" else int(str(x)[::-1])
        return x_reverse if x_reverse < (2 ** 31 - 1) and x_reverse > -(2 ** 31) else 0


if __name__ == '__main__':
    print(Solution().reverse(321))
