from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  # noqa
        return [int(digit) for digit in str(int(''.join(map(str, digits))) + 1)]


if __name__ == '__main__':
    print(Solution().plusOne([4, 3, 2, 1, 4]))
