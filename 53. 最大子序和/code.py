# 双指针法
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)

t = Solution()
print(t.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))