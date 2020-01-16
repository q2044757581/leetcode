class Solution:
    def maxArea(self, height):
        max_area = 0
        # 双指针
        p = 0
        q = len(height) - 1
        while 0 <= p < q < len(height):
            temp_area = (q - p) * min(height[p], height[q])
            if temp_area > max_area:
                max_area = temp_area
            if height[p] <= height[q]:
                p += 1
            else:
                q -= 1
        return max_area

t = Solution()
print(t.maxArea([1,8,6,2,5,4,8,3,7]))
print(t.maxArea([1,1]))