class Solution:
    def intToRoman(self, num):
        rank_num = [1000, 500, 100, 50, 10, 5, 1]
        rank_char = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        result = ""
        # 余数
        left = num
        for i in range(len(rank_num)):
            if int(left / rank_num[i]):
                # c x i 这三种特殊情况处理
                temp = int(left / rank_num[i])
                result += rank_char[i] * temp
                left = left % rank_num[i]
            # 判断M, C, X
            if i == 0 or i == 2 or i == 4:
                if left >= rank_num[i] - rank_num[i+2]:
                    result += rank_char[i+2] + rank_char[i]
                    left -= (rank_num[i] - rank_num[i+2])
            # 判断D,L,V
            elif i == 1 or i == 3 or i == 5:
                if left >= rank_num[i] - rank_num[i+1]:
                    result += rank_char[i+1] + rank_char[i]
                    left -= (rank_num[i] - rank_num[i + 1])
        return result

t = Solution()
print(t.intToRoman(1994))