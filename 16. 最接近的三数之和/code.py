class Solution:
    # 双指针法
    def threeSumClosest(self, nums, target):
        best_score = -1
        result = 0
        nums = sorted(nums)
        for i in range(len(nums)-2):
            p = i + 1
            q = len(nums) - 1
            while p < q:
                s = nums[i] + nums[p] + nums[q]
                score = s - target
                if abs(score) < best_score or best_score == -1:
                    best_score = abs(score)
                    result = s
                if s > target:
                    v = nums[q]
                    while p != q and nums[q] == v:
                        q -= 1
                elif s < target:
                    v = nums[p]
                    while p != q and nums[p] == v:
                        p += 1
                else:
                    break
        return result

t = Solution()
# print(t.threeSumClosest([-1,2,1,-4], 1))
# print(t.threeSumClosest([1, 1, 1, 1], 0))
print(t.threeSumClosest([1,2,4,8,16,32,64,128], 82))