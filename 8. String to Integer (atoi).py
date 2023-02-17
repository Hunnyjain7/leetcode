class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        negative = False
        positive = False
        negative_again = False
        positive_again = False
        new_str = ""
        started = False
        for i in s.strip():
            if i == "-" and not started:
                if negative:
                    negative_again = True
                negative = True
            elif i == "+" and not started:
                if positive:
                    positive_again = True
                positive = True
            else:
                try:
                    if negative_again or positive_again:
                        break
                    else:
                        new_str += str(int(i))
                        started = True
                except ValueError:
                    break
        if len(new_str) == 0:
            return 0
        if negative and positive:
            return 0
        int_new_str = -int(new_str) if negative else int(new_str)
        return - 2 ** 31 if int_new_str < -2 ** 31 else 2 ** 31 - 1 if int_new_str > 2 ** 31 - 1 else int_new_str


if __name__ == '__main__':
    print(Solution().myAtoi("   -42"))
