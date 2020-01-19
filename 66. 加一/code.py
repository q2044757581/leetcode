from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        left = 1
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + left
            digits[i] = temp % 10
            left = int(temp / 10)
            if left == 0:
                break
        if left:
            return [1] + digits
        else:
            return digits

t = Solution()
print(t.plusOne([9]))