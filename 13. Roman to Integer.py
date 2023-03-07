class Solution(object):
    def romanToInt(self, s):  # noqa
        """
        :type s: str
        :rtype: int
        """
        dic = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        num = 0
        skip = False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if skip:
                    skip = False
                    break
                elif j < len(s) and (s[i] + s[j]) in dic.keys():
                    num += dic[s[i] + s[j]]
                    skip = True
                elif s[i] in dic.keys():
                    num += dic[s[i]]
                break
        return num


if __name__ == '__main__':
    print(Solution().romanToInt("III"))
