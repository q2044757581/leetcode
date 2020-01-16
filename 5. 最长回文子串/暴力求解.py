# 不可取
class Solution:
    def longestPalindrome(self, s):
        max_len = 0
        result = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    if max_len < 1:
                        max_len = 1
                        result = s[i:j+1]
                else:
                    # 判断s[i,j]是不是回文子串
                    det = True
                    for k in range(i, int((j + i) / 2) + 1):
                        if s[k] != s[j+i-k]:
                            det = not det
                            break
                    if det:
                        if max_len < j - i + 1:
                            max_len = j - i + 1
                            result = s[i:j+1]
        return result


t = Solution()
print(t.longestPalindrome("cbbd"))

