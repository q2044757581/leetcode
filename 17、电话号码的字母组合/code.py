from typing import List


class Solution:
    def __init__(self):
        self.map_val = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                        '8': "tuv", '9': "wxyz"}

    def getCombinations(self, digits, start_pos, result):
        temp = []
        for i in range(len(self.map_val[digits[start_pos]])):
            # 对之前的记录都加上该位的n种可能
            for item in result:
                temp.append(item + self.map_val[digits[start_pos]][i])
        return temp

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = list(self.map_val[digits[0]])
        # 初始化
        if len(digits) >= 2:
            for i in range(1, len(digits)):
                result = self.getCombinations(digits, i, result)
        return result

t = Solution()
print(t.letterCombinations("23"))

