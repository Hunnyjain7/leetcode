class Solution:
    def addBinary(self, a: str, b: str) -> str:  # noqa
        sum_val = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            sum_val += str(carry % 2)
            carry //= 2
        return sum_val[::-1]

    # not mine
    def addBinary2(self, a: str, b: str) -> str:  # noqa
        return f"{int(a, 2) + int(b, 2):b}"


if __name__ == '__main__':
    print(Solution().addBinary("1010", "1011"))
