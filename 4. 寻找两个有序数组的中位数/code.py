class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = sorted(nums1 + nums2)
        length = len(nums1)
        if length % 2 == 0:
            return (nums1[int(length / 2)] + nums1[int(length / 2) - 1]) / 2
        else:
            return nums1[int(length / 2)]

nums1 = [1, 3]
nums2 = [2, 4]
t = Solution()
print(t.findMedianSortedArrays(nums1, nums2))