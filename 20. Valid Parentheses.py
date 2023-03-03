class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "small": {
                "open": 0,
                "close": 0,
                "is_opened": 0
            },
            "curly": {
                "open": 0,
                "close": 0,
                "is_opened": 0
            },
            "big": {
                "open": 0,
                "close": 0,
                "is_opened": 0
            }
        }
        brackets = {
            "(": "small_open",
            ")": "small_close",
            "{": "curly_open",
            "}": "curly_close",
            "[": "big_open",
            "]": "big_close"
        }
        small_open = False
        curly_open = False
        big_open = False
        for i in s:
            value = brackets[i].split('_')
            # if value[1] == "open":
            if value[0] == "small":
                if small_open:
                    small_open = False
                else:
                    small_open = True
            if value[0] == "curly":
                if curly_open:
                    curly_open = False
                else:
                    curly_open = True
            if value[0] == "big":
                if big_open:
                    big_open = False
                else:
                    big_open = True

            if value[1] == "open":
                dic[value[0]]["is_opened"] += 1

            if small_open:
                if value[0] == "curly" and value[1] == "close":
                    return False
                if value[0] == "big" and value[1] == "close":
                    return False
            if curly_open:
                if value[0] == "big" and value[1] == "close":
                    return False

            if value[0] == "small" and small_open and value[1] == "close":
                if dic[value[0]]["is_opened"] > dic[value[0]][value[1]]:
                    dic[value[0]][value[1]] += 1
            elif value[0] == "curly" and curly_open and value[1] == "close":
                if small_open:
                    return False
                if dic[value[0]]["is_opened"] > dic[value[0]][value[1]]:
                    dic[value[0]][value[1]] += 1
            elif value[0] == "big" and big_open and value[1] == "close":
                if curly_open and small_open:
                    return False
                if dic[value[0]]["is_opened"] > dic[value[0]][value[1]]:
                    dic[value[0]][value[1]] += 1
            else:
                if dic[value[0]]["is_opened"] > dic[value[0]][value[1]]:
                    dic[value[0]][value[1]] += 1

        print(dic)
        if dic["small"]["open"] != dic["small"]["close"]:
            return False
        if dic["curly"]["open"] != dic["curly"]["close"]:
            return False
        if dic["big"]["open"] != dic["big"]["close"]:
            return False
        return True


if __name__ == '__main__':
    print(Solution().isValid("([)]"))
