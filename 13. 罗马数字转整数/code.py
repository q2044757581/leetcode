"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
"""
class Solution:
    def romanToInt(self, s):
        sum_val = 0
        val_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            # 看后面有没有V或X
            if s[i] == 'I':
                if 'V' in s[i+1:] or 'X' in s[i+1:]:
                    sum_val -= val_map[s[i]]
                else:
                    sum_val += val_map[s[i]]
            elif s[i] == 'X':
                if 'L' in s[i+1:] or 'C' in s[i+1:]:
                    sum_val -= val_map[s[i]]
                else:
                    sum_val += val_map[s[i]]
            elif s[i] == 'C':
                if 'D' in s[i+1:] or 'M' in s[i+1:]:
                    sum_val -= val_map[s[i]]
                else:
                    sum_val += val_map[s[i]]
            else:
                sum_val += val_map[s[i]]
        return sum_val
t = Solution()
print(t.romanToInt("III"))
print(t.romanToInt("MCMXCIV"))
print(t.romanToInt("LVIII"))