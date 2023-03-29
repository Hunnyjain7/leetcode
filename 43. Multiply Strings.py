class Solution:
    def multiply(self, num1: str, num2: str) -> str:  # noqa
        mapper = {f"{i}": "|" * i for i in range(10)}
        num1_c, num2_c = 0, 0
        num1_len, num2_len = len(num1) - 1, len(num2) - 1
        for i in num2:
            num2_c += len(mapper[i]) * (10 ** num2_len)
            num2_len -= 1
        for i in num1:
            num1_c += len(mapper[i]) * (10 ** num1_len)
            num1_len -= 1
        return str(num2_c * num1_c)


if __name__ == '__main__':
    print(Solution().multiply("123", "456"))
