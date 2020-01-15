class Solution:
    def myAtoi(self, str):
        temp = list(str.strip())
        temp2 = []
        det = False
        for i in range(len(temp)):
            if '0' <= temp[i] <= '9':
                det = True
                if i != 0:
                    if temp[i-1] == '+' or temp[i-1] == '-':
                        temp2.append(temp[i-1])
                temp2.append(temp[i])
            elif temp[i] == '.':
                if i!=0 and i!=len(temp)-1:
                    if '0' <= temp[i-1] <= '9' and '0' <= temp[i+1] <= '9':
                        temp2.append(temp[i])
                if i==0 and i!=len(temp)-1:
                    if '0' <= temp[i + 1] <= '9':
                        temp2.append('0')
                        temp2.append(temp[i])
            elif ('a' <= temp[i] <= 'z' or 'A' <= temp[i] <= 'Z') and not det:
                return 0
        if not temp2 or not det:
            return 0
        try:
            temp2 = int(eval("".join(temp2)))
        except:
            temp2 = int("".join(temp2))
        if temp2 < -2147483648:
            temp2 = -2147483648
        elif temp2 > 2147483647:
            temp2 = 2147483647
        return temp2

t = Solution()
print(t.myAtoi(".1"))


