from typing import List


class Solution:
    permutation = []

    def nextPermutation(self, nums: List[int]) -> None:  # noqa
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)

        def rev(nums, start):  # noqa
            end = nums_len - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        i = nums_len - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = nums_len - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        rev(nums, i + 1)

    # tried sol not worked
    def nextPermutation3(self, nums: List[int]):  # noqa
        """
        """
        dummy = nums.copy()
        nums.sort()
        self.perm(nums, [], dummy)
        take = False
        for i in self.permutation:
            if take:
                nums = i
                break
            if i == dummy:
                take = True

    def perm(self, start, end=[], dummy=None):
        if len(start) == 0:
            self.permutation.append(end)
        else:
            for i in range(len(start)):
                self.perm(start[:i] + start[i + 1:], end + start[i:i + 1], dummy)

    # tried sol not worked
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
