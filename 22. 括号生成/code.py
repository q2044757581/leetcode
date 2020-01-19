from typing import List

# 递归
class Solution:
    def getstr(self, n):
        if n == 0:
            return [""]
        elif n == 1:
            return ["()"]
        else:
            # 三种可能， 括起来， 放左边， 放右边
            result = []
            for i in range(n):
                p = i
                q = n - 1 - p
                temp1 = self.getstr(p)
                temp2 = self.getstr(q)
                for item1 in temp1:
                    for item2 in temp2:
                        result.append("("+item1+")"+item2)
            return result

    """
        "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】
        其中 p + q = n-1，且 p q 均为非负整数。
        事实上，当上述 p 从 0 取到 n-1，q 从 n-1 取到 0 后，所有情况就遍历完了。
    """
    def generateParenthesis(self, n: int) -> List[str]:
        return self.getstr(n)

t = Solution()
print(t.generateParenthesis(3))
