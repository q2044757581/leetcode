class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        elif len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        else:
            print("lala")
            result = -1
            for i in range(len(haystack) - len(needle) + 1):
                print(haystack[i])
                if haystack[i:(i+len(needle))] == needle:
                    result = i
                    break
            return result
t = Solution()
print(t.strStr("hello", 'll'))