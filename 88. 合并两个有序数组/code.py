from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = 0
        nums1_len = m
        for i in range(len(nums1)):
            if p < n:
                if nums1[i] >= nums2[p]:
                    # nums1后移
                    for j in range(len(nums1) - 1, i, -1):
                        nums1[j] = nums1[j-1]
                    nums1[i] = nums2[p]
                    nums1_len += 1
                    p += 1
            else:
                break
        # 对剩下的部分进行填补
        for i in range(nums1_len, len(nums1)):
            if p < n:
                # nums1后移
                for j in range(len(nums1) - 1, i, -1):
                    nums1[j] = nums1[j - 1]
                nums1[i] = nums2[p]
                nums1_len += 1
                p += 1
