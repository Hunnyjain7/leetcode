class Solution:
    def search(self, nums: List[int], target: int) -> bool:  # noqa
        return target in nums


if __name__ == '__main__':
    print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
