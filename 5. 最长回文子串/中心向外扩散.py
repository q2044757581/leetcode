"""
1）将子串分为单核和双核的情况，单核即指子串长度为奇数，双核则为偶数；

2）遍历每个除最后一个位置的字符index(字符位置)，单核：初始low = 初始high = index，low和high均不超过原字符串的下限和上限；
判断low和high处的字符是否相等，相等则low--、high++（双核：初始high = 初始low+1 = index + 1）；

3）每次low与high处的字符相等时，都将当前最长的回文子串长度与high-low+1比较。后者大时，将最长的回文子串改为low与high之间的；

4）重复执行2）、3），直至high-low+1 等于原字符串长度或者遍历到最后一个字符，取当前截取到的回文子串，该子串即为最长的回文子串。
"""


class Solution:
    def __init__(self):
        self.sub = ""

    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        for k in range(len(s) - 1):
            self.findLongestPalindrome(s, k, k)
            self.findLongestPalindrome(s, k, k+1)
        return self.sub

    def findLongestPalindrome(self, s, i, j):
        low = i
        high = j
        while low >= 0 and high <= len(s) - 1:
            if s[low] == s[high]:
                if high - low + 1 > len(self.sub):
                    self.sub = s[low:high+1]
                    if len(self.sub) == len(s):
                        break
                low -= 1
                high += 1
            else:
                break


t = Solution()
print(t.longestPalindrome("cbbd"))
print(t.longestPalindrome("babad"))