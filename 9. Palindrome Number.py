class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return True if str(x) == str(x)[::-1] else False


if __name__ == '__main__':
    print(Solution().isPalindrome(-121))
