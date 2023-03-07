from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  # noqa
        arr = nums1 + nums2
        arr_len = len(arr)
        for i in range(arr_len):
            curr = i
            while curr < arr_len:
                if arr[curr] < arr[i]:
                    arr[curr], arr[i] = arr[i], arr[curr]
                curr += 1
        return (
            float(arr[(arr_len // 2)])
            if bool(arr_len % 2)
            else float((arr[(arr_len // 2)] + arr[(arr_len // 2) - 1]) / 2)
        )


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
