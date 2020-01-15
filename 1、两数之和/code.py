class Solution:
    def twoSum(self, nums, target):
        Map = {}
        for i in range(len(nums)):
            if target - nums[i] in Map:
                return [Map[target - nums[i]], i]
            Map[nums[i]] = i


t = Solution()
print(t.twoSum([2, 7, 11, 15], 9))