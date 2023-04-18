class Solution:
    def isValid(self, s: str) -> bool:  # noqa
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return False if len(s) != 0 else True

    def isValid2(self, s: str) -> bool:  # noqa
        CLOSING = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        st = []
        for c in s:
            if c in CLOSING:
                st.append(CLOSING[c])
            elif not st or c != st.pop():
                return False
        return not st


if __name__ == '__main__':
    print(Solution().isValid("({[]})"))
    # print(dict(('()', '[]', '{}')))

# Failed attempts
# class Solution:
#     def isValid(self, s: str) -> bool:
#         first = 0
#         last = len(s) - 1
#         while first < last:
#             temp = first
#             small_open = False
#             curly_open = False
#             big_open = False
#             while temp < last:
#                 if s[last] == ")":
#                     if s[temp] == "(":
#                         small_open = True
#                     elif s[temp] == "{":
#                         curly_open = True
#                     elif s[temp] == "[":
#                         big_open = True
#                     elif s[temp] == "]":
#                         big_open = False
#                     elif s[temp] == "}":
#                         curly_open = False
#                     elif s[temp] == ")":
#                         small_open = False
#                 if s[last] == "}":
#                     if s[temp] == "(":
#                         small_open = True
#                     elif s[temp] == "{":
#                         curly_open = True
#                     elif s[temp] == "[":
#                         big_open = True
#                     elif s[temp] == "]":
#                         big_open = False
#                     elif s[temp] == "}":
#                         curly_open = False
#                     elif s[temp] == ")":
#                         small_open = False
#                 if s[last] == "]":
#                     if s[temp] == "(":
#                         small_open = True
#                     elif s[temp] == "{":
#                         curly_open = True
#                     elif s[temp] == "[":
#                         big_open = True
#                     elif s[temp] == "]":
#                         big_open = False
#                     elif s[temp] == "}":
#                         curly_open = False
#                     elif s[temp] == ")":
#                         small_open = False
#                 temp += 1
#             if s[last] == ")":
#                 small_open = False
#             if s[last] == "}":
#                 curly_open = False
#             if s[last] == "]":
#                 big_open = False
#             if small_open or big_open or curly_open:
#                 return False
#             last -= 1
#             first += 1
#         return True

# dic = {
#     "small": {
#         "open": 0,
#         "close": 0,
#         "is_opened": 0,
#         "index": None
#     },
#     "curly": {
#         "open": 0,
#         "close": 0,
#         "is_opened": 0,
#         "index": None
#     },
#     "big": {
#         "open": 0,
#         "close": 0,
#         "is_opened": 0,
#         "index": None
#     }
# }
# brackets = {
#     "(": "small_open",
#     ")": "small_close",
#     "{": "curly_open",
#     "}": "curly_close",
#     "[": "big_open",
#     "]": "big_close"
# }
# small_open = False
# curly_open = False
# big_open = False
# index = 0
# for i in s:
#     value = brackets[i].split('_')
#     if value[1] == "open":
#         dic[value[0]]["is_opened"] += 1
#         dic[value[0]]["index"] = index
#
#     if value[0] == "small" and small_open and value[1] == "close":
#         if dic[value[0]]["is_opened"] > dic[value[0]][value[1]]:
#             dic[value[0]][value[1]] += 1
#             if (dic["big"]["index"] and dic[value[0]]["index"] < dic["big"]["index"]) or (
#                     dic["curly"]["index"] and dic[value[0]]["index"] < dic["curly"]["index"]):
#                 return False
#         dic[value[0]]["index"] = None
#     elif value[0] == "curly" and curly_open and value[1] == "close":
#         if small_open:
#             return False
#         if dic[value[0]]["is_opened"] > dic[value[0]][value[1]]:
#             dic[value[0]][value[1]] += 1
#             if (dic["big"]["index"] and dic[value[0]]["index"] < dic["big"]["index"]) or (
#                     dic["small"]["index"] and dic[value[0]]["index"] < dic["small"]["index"]):
#                 return False
#             dic[value[0]]["index"] = None
#     elif value[0] == "big" and big_open and value[1] == "close":
#         if curly_open and small_open:
#             return False
#         if dic[value[0]]["is_opened"] > dic[value[0]][value[1]]:
#             dic[value[0]][value[1]] += 1
#             if (dic["curly"]["index"] and dic[value[0]]["index"] < dic["curly"]["index"]) or (
#                     dic["small"]["index"] and dic[value[0]]["index"] < dic["small"]["index"]):
#                 return False
#             dic[value[0]]["index"] = None
#     else:
#         if dic[value[0]]["is_opened"] > dic[value[0]][value[1]]:
#             dic[value[0]][value[1]] += 1
#             # dic[value[0]]["index"] = 0
#
#     if value[0] == "small":
#         if value[1] == "close":
#             small_open = False
#         else:
#             small_open = True
#     if value[0] == "curly":
#         if value[1] == "close":
#             curly_open = False
#         else:
#             curly_open = True
#     if value[0] == "big":
#         if value[1] == "close":
#             big_open = False
#         else:
#             big_open = True
#
#     if small_open:
#         if value[0] == "curly" and value[1] == "close":
#             return False
#         if value[0] == "big" and value[1] == "close":
#             return False
#     if curly_open:
#         if value[0] == "big" and value[1] == "close":
#             return False
#     index += 1
#
# print(dic)
# if dic["small"]["open"] != dic["small"]["close"]:
#     return False
# if dic["curly"]["open"] != dic["curly"]["close"]:
#     return False
# if dic["big"]["open"] != dic["big"]["close"]:
#     return False
# return True
