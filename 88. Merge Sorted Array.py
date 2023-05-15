from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # noqa
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        print(nums1)

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # noqa
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = 0
        for i in range(m, m + n):
            nums1[i] = nums2[count]
        count += 1
        nums1.sort()


if __name__ == '__main__':
    print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
