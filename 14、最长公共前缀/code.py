class Solution:
    def longestCommonPrefix(self, strs):
        min_len = -1
        for item in strs:
            if min_len == -1:
                min_len = len(item)
            elif len(item) < min_len:
                min_len = len(item)
        result = ""
        for i in range(min_len):
            pattern = strs[0][:i+1]
            det = True
            for j in range(1, len(strs)):
                if strs[j][:i+1] != pattern:
                    det = False
                    break
            if det:
                result = pattern
            else:
                break
        return result
t = Solution()
print(t.longestCommonPrefix(["dog","racecar","car"]))