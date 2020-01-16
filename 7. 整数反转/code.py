class Solution:
    def reverse(self, x):
        result = 0
        x = str(x)
        if x[0] == '-':
            val = x[1:]
            result = -int(val[::-1])
        else:
            result = int(x[::-1])
        return result if 2**31 - 1 >= result >= -2**31 else 0

t = Solution()
print(t.reverse("-321"))