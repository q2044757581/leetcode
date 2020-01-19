from typing import List


# 迭代
class Solution:
    """
        "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】
        其中 p + q = n-1，且 p q 均为非负整数。
        事实上，当上述 p 从 0 取到 n-1，q 从 n-1 取到 0 后，所有情况就遍历完了。
    """
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n == 0:
            return []
        for i in range(n+1):
            if i == 0:
                result.append([""])
            elif i == 1:
                result.append(["()"])
            else:
                l = []
                for j in range(i):
                    p = j
                    q = i - 1 - p
                    temp1 = result[p]
                    temp2 = result[q]
                    for item1 in temp1:
                        for item2 in temp2:
                            l.append("(" + item1 + ")" + item2)

                result.append(l)
        return result[-1]

t = Solution()
print(t.generateParenthesis(3))