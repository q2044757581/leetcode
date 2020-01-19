class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        # 二分法查找
        p = 1
        q = x
        while p <= q:
            r = int((p + q) / 2)
            if r ** 2 == x:
                return r
            elif r ** 2 < x:
                p = r + 1
            else:
                q = r - 1
        return p - 1

t = Solution()
print(t.mySqrt(5))