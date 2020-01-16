class Solution:
    def myAtoi(self, str):
        str = str.strip()
        if str == "":
            return 0
        det = True
        if str[0] == '-' or str[0] == '+' or '0' <= str[0] <= '9':
            result = ""
            for i in range(len(str)):
                # 是否里面有数字
                if '0' <= str[i] <= '9':
                    det = False
                # +- 号后面一定要加数字
                if str[i] == "+" or str[i] == '-':
                    if i == len(str) - 1:
                        return 0
                    elif not "0" <= str[i+1] <= "9":
                        return 0
                # 保留对结果有影响的符号和数字
                if str[i] == '-' or '0' <= str[i] <= '9' or str[i] == '.':
                    result += str[i]
                # 如果数字后面接的是其他字符， break
                if '0' <= str[i] <= '9':
                    if i != len(str) - 1:
                        if not '0' <= str[i+1] <= '9':
                            break
        else:
            return 0
        if det:
            return 0
        # int 范围限制
        if result[0] == '-':
            result = -int(float(result[1:]))
        else:
            result = int(float(result))
        if result < - 2 ** 31:
            return - 2 ** 31
        elif result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return result

t = Solution()
print(t.myAtoi(" -42"))