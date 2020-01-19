class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p = len(a) - 1
        q = len(b) - 1
        result = ""
        left = 0
        while p >= 0 and q >= 0:
            temp = int(a[p]) + int(b[q]) + left
            result += str(temp % 2)
            left = int(temp / 2)
            p -= 1
            q -= 1

        while p >= 0:
            temp = int(a[p]) + left
            result += str(temp % 2)
            left = int(temp / 2)
            p -= 1

        while q >= 0:
            temp = int(b[q]) + left
            result += str(temp % 2)
            left = int(temp / 2)
            q -= 1

        if left:
            result += "1"
        return result[::-1]

t = Solution()
print(t.addBinary("11", "1"))



