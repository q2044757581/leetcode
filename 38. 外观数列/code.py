class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(n - 1):
            last_str = result
            temp = ""
            start_pos = 0
            cnt = 0
            for j in range(len(last_str)):
                if last_str[j] == last_str[start_pos]:
                    cnt += 1
                else:
                    temp += (str(cnt) + last_str[start_pos])
                    start_pos = j
                    cnt = 1
            temp += (str(cnt) + last_str[start_pos])
            result = temp
        return result

t = Solution()
for i in range(1, 6):
    print(t.countAndSay(i))