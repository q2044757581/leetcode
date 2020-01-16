# 暴力两层循环
class Solution:
    def maxArea(self, height):
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                tmp_area = (j-i) * min(height[i], height[j])
                if max_area < tmp_area:
                    max_area = tmp_area
        return max_area

t = Solution()
print(t.maxArea([1,8,6,2,5,4,8,3,7]))
print(t.maxArea([1,1]))