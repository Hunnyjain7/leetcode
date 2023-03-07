class Solution:
    def intToRoman(self, num: int) -> str:  # noqa
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

        output = ""
        for key, value in dic.items():
            output += key * (num // value)
            if num // value != 0:
                num -= (value * (num // value))

        return output


if __name__ == '__main__':
    sol = Solution()
    print(sol.intToRoman(1994))

# My solution
# class Solution(object):
#     data = {
#         1: "I",
#         4: "IV",
#         5: "V",
#         9: "IX",
#         10: "X",
#         40: "XL",
#         50: "L",
#         90: "XC",
#         100: "C",
#         400: "CD",
#         500: "D",
#         900: "CM",
#         1000: "M",
#         1900: "MCM",
#         2900: "MMCM",
#         3900: "MMMCM",
#     }
#     roman = ""
#
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         num_str = str(num)
#         num_len = len(num_str)
#         if num_len > 0 and num > 0:
#             if self.data.get(num, False):
#                 self.roman = self.roman + self.data.get(num)
#             elif num_len == 1:
#                 if (num > 0) and (num < 4):
#                     self.roman = self.roman + (self.data[1] * num)
#                 elif num == 4:
#                     self.roman = self.roman + self.data[4]
#                 elif num == 5:
#                     self.roman = self.roman + self.data[5]
#                 elif (num > 5) and (num < 9):
#                     self.roman = self.roman + self.data[5] + (self.data[1] * (num - 5))
#                 elif num == 9:
#                     self.roman = self.roman + self.data[9]
#             elif num_len == 2:
#                 if (num > 10) and (num < 40):
#                     self.roman = self.roman + (self.data[10] * int(num_str[0]))
#                     self.intToRoman(int(num_str[1]))
#                 elif (num > 40) and (num < 50):
#                     self.roman = self.roman + self.data[40]
#                     self.intToRoman(num - 40)
#                 elif (num > 50) and (num < 90):
#                     self.roman = self.roman + self.data[50]
#                     self.intToRoman(num - 50)
#                 else:
#                     self.roman = self.roman + self.data[90]
#                     self.intToRoman(num - 90)
#             elif num_len == 3:
#                 if (num > 100) and (num < 400):
#                     self.roman = self.roman + self.data[100]
#                     self.intToRoman(num - 100)
#                 elif (num > 400) and (num < 500):
#                     self.roman = self.roman + self.data[400]
#                     self.intToRoman(num - 400)
#                 elif (num > 500) and (num < 900):
#                     self.roman = self.roman + self.data[500]
#                     self.intToRoman(num - 500)
#                 elif (num > 900) and (num < 1000):
#                     self.roman = self.roman + self.data[900]
#                     self.intToRoman(num - 900)
#             else:
#                 if (num > 1000) and (num < 1900):
#                     self.roman = self.roman + self.data[1000]
#                     self.intToRoman(num - 1000)
#                 elif (num > 1900) and (num < 2000):
#                     self.roman = self.roman + self.data[1900]
#                     self.intToRoman(num - 1900)
#                 elif (num > 2000) and (num < 2900):
#                     self.roman = self.roman + (self.data[1000] * 2)
#                     self.intToRoman(num - 2000)
#                 elif (num > 2900) and (num < 3000):
#                     self.roman = self.roman + self.data[2900]
#                     self.intToRoman(num - 2900)
#                 elif (num > 3000) and (num < 3900):
#                     self.roman = self.roman + (self.data[1000] * 3)
#                     self.intToRoman(num - 3000)
#                 elif (num > 3900) and (num < 4000):
#                     self.roman = self.roman + self.data[3900]
#                     self.intToRoman(num - 3900)
#                 else:
#                     self.roman = self.roman + (self.data[1000] * int(num_str[0]))
#                     self.intToRoman(num - (1000 * int(num_str[0])))
#         return self.roman

# better Solutions from leetcode
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         dic = {
#             "M": 1000,
#             "CM": 900,
#             "D": 500,
#             "CD": 400,
#             "C": 100,
#             "XC": 90,
#             "L": 50,
#             "XL": 40,
#             "X": 10,
#             "IX": 9,
#             "V": 5,
#             "IV": 4,
#             "I": 1
#         }
#
#         output = ""
#         for key, value in dic.items():
#             output += key * (num // value)
#             if num // value != 0:
#                 num -= (value * (num // value))
#
#         return output

# My failure attempt
# class Solution(object):
#     data = {
#         1: "I",
#         5: "V",
#         10: "X",
#         50: "L",
#         100: "C",
#         500: "D",
#         1000: "M"
#     }
#
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         new_num = ""
#         previous = None
#         for key, value in self.data.items():
#             if previous is None:
#                 previous = key
#             if num == key:
#                 return value
#             elif (num > previous) and (num < key):
#                 num_str = str(num)
#                 i = len(str(num)) - 1
#                 while i >= 0:
#                     num_int = int(num_str[i])
#                     if num_int == 0:
#                         zeros = 0
#                         j = len(str(num)) - 1
#                         while j >= 0:
#                             if int(num_str[i]) == 0:
#                                 zeros += 1
#                                 j -= 1
#                             else:
#                                 break
#                         if zeros == 1 and num <
#                     if (num_int > 0) and (num_int < 4):
#                         new_num = new_num + self.data[1] * num_int
#                     elif num_int == 4:
#                         new_num = new_num + self.data[1] + self.data[5]
#                     elif num_int == 5:
#                         new_num = new_num + self.data[5]
#                     elif (num_int > 5) and (num_int < 9):
#                         new_num = new_num + self.data[5] + (self.data[1] * num_int)
#                     if (num_int > 0) and (num_int < 4):
#                         new_num = new_num + self.data[1] * num_int
#                     if (num_int > 0) and (num_int < 4):
#                         new_num = new_num + self.data[1] * num_int
#
#                     i -= 1
#
#                 print(previous, key)
#             previous = key
#         return new_num
