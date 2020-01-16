class Solution:
    def threeSum(self, nums):
        result = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            # 固定一个数， 变为twosum问题
            """
            1.当 nums[k] > 0 时直接break跳出：因为 nums[j] >= nums[i] >= nums[k] > 0，即 333 个数字都大于 000 ，在此
            固定指针 k 之后不可能再找到结果了。
            2.当 k > 0且nums[k] == nums[k - 1]时即跳过此元素nums[k]：因为已经将 nums[k - 1] 的所有组合加入到结果中，
            本次双指针搜索只会得到重复组合。
            3.i，j 分设在数组索引 (k,len(nums))(k, len(nums))(k,len(nums)) 两端，当i < j时循环计算s = nums[k] + nums[i]
             + nums[j]，并按照以下规则执行双指针移动：

            当s < 0时，i += 1并跳过所有重复的nums[i]；
            当s > 0时，j -= 1并跳过所有重复的nums[j]；
            当s == 0时，记录组合[k, i, j]至res，执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，防止记录到重复组合。
            """
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                p = i + 1
                q = len(nums) - 1
                while p < q:
                    s = nums[i] + nums[p] + nums[q]
                    if s > 0:
                        v = nums[q]
                        while p != q and nums[q] == v:
                            q -= 1
                    elif s < 0:
                        v = nums[p]
                        while p != q and nums[p] == v:
                            p += 1
                    else:
                        result.append([nums[i], nums[p], nums[q]])
                        v = nums[q]
                        while p != q and nums[q] == v:
                            q -= 1
                        v = nums[p]
                        while p != q and nums[p] == v:
                            p += 1
        return result

t = Solution()
print(t.threeSum([0, 0, 0, 0]))
print(t.threeSum([-1, 0, 1, 2, -1, -4]))