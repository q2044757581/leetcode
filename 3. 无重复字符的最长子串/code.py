class Solution:
    def lengthOfLongestSubstring(self, s):
        already = {}
        max_len = 0
        start = 0
        len_s = len(s)
        # 一直更新每个字符的出现位置
        for i in range(len_s):
            if s[i] not in already:
                already[s[i]] = i
            elif already[s[i]] >= start:
                # 取更大值
                max_len = max(max_len, i - start)
                # 因为从already[s[i]] 到 i 的首尾重复了, 那么从already[s[i]]+1开始是不重复的字符串
                start = already[s[i]] + 1
                already[s[i]] = i
            else:
                already[s[i]] = i
        return max(max_len, len_s - start)


t = Solution()
print(t.lengthOfLongestSubstring("abcabcbb"))
print(t.lengthOfLongestSubstring(" "))
print(t.lengthOfLongestSubstring("pwwkew"))
print(t.lengthOfLongestSubstring("dvdf"))
print(t.lengthOfLongestSubstring("aaa"))
print(t.lengthOfLongestSubstring("abba"))
print(t.lengthOfLongestSubstring("aabaab!bb"))