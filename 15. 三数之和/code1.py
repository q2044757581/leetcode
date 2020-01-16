# O(n**2)
class Solution:
    def threeSum(self, nums):
        result = []
        Map = {}
        nums = sorted(nums)
        for i in range(len(nums)-2):
            # 固定一个数， 变为twosum问题
            Map = {}
            target = -nums[i]
            for j in range(i + 1, len(nums)):
                if target - nums[j] in Map:
                    # 判断有没有重复，若没有重复则放入result
                    temp = [nums[i], target - nums[j], nums[j]]
                    if temp not in result:
                        result.append(temp)
                Map[nums[j]] = j
        return result

t = Solution()
print(t.threeSum([0, 0, 0, 0]))