from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_copy = intervals.copy()
        break_it = False
        for i in range(len(intervals)):
            # if break_it:
            #     break_it = False
            #     break
            for j in range(i + 1, len(intervals) - 1):
                FAFV, FASV, SAFV, SASV = (
                    intervals[i][0],
                    intervals[i][1],
                    intervals[j][0],
                    intervals[j][1],
                )
                print("FAFV, SAFV", FAFV, SAFV)
                if FAFV > SAFV:
                    FAFV, SAFV = SAFV, FAFV
                if FASV > SASV:
                    FASV, SASV = SASV, FASV
                print("FAFV, SAFV", FAFV, SAFV)
                interval_range = range(FAFV, SASV + 1)
                FA_interval_range = range(FAFV, FASV + 1)
                SA_interval_range = range(SAFV, SASV + 1)

                if (
                        FASV in SA_interval_range and SAFV in FA_interval_range
                        and FASV in interval_range and SAFV in interval_range
                ):
                    intervals_copy[i:j + 1] = [[FAFV, SASV]]

                # break_it = True
                # break

        return intervals_copy


if __name__ == '__main__':
    # print(Solution().merge([[4,5],[1,4],[0,1]]))
    print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))

# if len(intervals) > 1:
#     FAFV, FASV, SAFV, SASV = (
#         intervals[-2][-2],
#         intervals[-2][-1],
#         intervals[-1][-2],
#         intervals[-1][-1],
#     )
#     if FAFV > SAFV:
#         FAFV, SAFV = SAFV, FAFV
#     if FASV > SASV:
#         FASV, SASV = SASV, FASV
#     interval_range = range(FAFV, SASV + 1)
#     FA_interval_range = range(FAFV, FASV + 1)
#     SA_interval_range = range(SAFV, SASV + 1)
#
#     if (
#             FASV in SA_interval_range and SAFV in FA_interval_range
#             and FASV in interval_range and SAFV in interval_range
#     ):
#         intervals[-2:] = [[FAFV, SASV]]
