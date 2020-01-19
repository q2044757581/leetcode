from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        # 固定一个数， 变成3数之和问题
        for i in range(len(nums) - 3):
            if nums[i] > target > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                for j in range(i+1, len(nums) - 2):
                    # 再固定一个数， 变成2数之和问题
                    if j > i+1 and nums[j] == nums[j - 1]:
                        continue
                    else:
                        p = j + 1
                        q = len(nums) - 1
                        while p < q:
                            s = nums[i] + nums[j] + nums[p] + nums[q]
                            if s > target:
                                v = nums[q]
                                while p != q and nums[q] == v:
                                    q -= 1
                            elif s < target:
                                v = nums[p]
                                while p != q and nums[p] == v:
                                    p += 1
                            else:
                                result.append([nums[i], nums[j], nums[p], nums[q]])
                                v = nums[q]
                                while p != q and nums[q] == v:
                                    q -= 1
                                v = nums[p]
                                while p != q and nums[p] == v:
                                    p += 1
        return result

t = Solution()
print(t.fourSum([1,-2,-5,-4,-3,3,3,5], -11))