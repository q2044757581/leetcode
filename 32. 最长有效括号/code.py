class Solution:
    def calc1(self, s):
        cnt = 0
        max_val = 0
        currLen = 0
        validLen = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                cnt += 1
            else:
                cnt -= 1
            currLen += 1
            if cnt < 0:
                max_val = max_val if max_val > validLen else validLen
                cnt = 0
                currLen = 0
                validLen = 0
            elif cnt == 0:
                validLen = currLen
        return max(max_val, validLen)

    def calc2(self, s):
        cnt = 0
        max_val = 0
        currLen = 0
        validLen = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                cnt += 1
            else:
                cnt -= 1
            currLen += 1
            if cnt < 0:
                max_val = max_val if max_val > validLen else validLen
                cnt = 0
                currLen = 0
                validLen = 0
            elif cnt == 0:
                validLen = currLen
        return max(max_val, validLen)

    def longestValidParentheses(self, s):
        return max(self.calc1(s), self.calc2(s))

t = Solution()
print(t.longestValidParentheses("()())"))