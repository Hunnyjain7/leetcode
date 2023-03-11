from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:  # noqa
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        permutations = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pass


    def nextPermutation2(self, nums: List[int]) -> None:  # noqa
        """
        Do not return anything, modify nums in-place instead.
        """
        is_permutation = False
        nums_len = len(nums)
        for i in range(nums_len):
            nex = i + 1
            if nex < nums_len and nums[i] <= nums[nex]:
                nexnex = nex + 1
                while nexnex < nums_len:
                    if nums[nex] < nums[nexnex]:
                        nums[nex], nums[nexnex] = nums[nexnex], nums[nex]
                        is_permutation = True
                        break
                    nexnex += 1
            if nex == nums_len - 1 and not is_permutation:
                num = nums[0]
                sorted_nums = sorted(nums)
                print(nums)
                print(sorted_nums)
                next_largest_num = None
                got = False
                for k in range(len(sorted_nums)):
                    if got:
                        break
                    l = k + 1
                    if l < nums_len and sorted_nums[k] == num:
                        while sorted_nums[l] == num:
                            l += 1
                        next_largest_num = sorted_nums[l]
                        got = True  # noqa
                        break
                print(next_largest_num)

                for j in range(len(nums)):
                    if nums[j] == next_largest_num:
                        nums[1], nums[j] = next_largest_num, nums[1]
                        break

            if is_permutation:
                break
        return nums  # noqa


# [2,1,3]
if __name__ == '__main__':
    print(Solution().nextPermutation([1, 3, 2]))
