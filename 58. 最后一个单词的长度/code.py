class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        start_pos = 0
        over_pos = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                over_pos = i
                break
        for i in range(over_pos - 1, -1, -1):
            if s[i] == " ":
                return over_pos - i
        return over_pos + 1

t = Solution()
print(t.lengthOfLastWord(" a"))