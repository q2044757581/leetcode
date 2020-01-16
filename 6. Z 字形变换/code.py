class Solution:
    def convert(self, s, numRows):
        z_len = max(int(numRows * 2 - 2), 1)
        result = ""
        rec = ["" for i in range(numRows)]
        for j in range(len(s)):
            index = int(min(int(j % z_len), int(z_len - j % z_len)))
            rec[index] += (s[j])
            # if j % z_len == i or j % z_len == z_len - i:
            #     result += s
        for j in range(numRows):
            result += rec[j]
        return result


t = Solution()
print(t.convert("LEETCODEISHIRING", 3))
# LCIRETOESIIGEDHN
print(t.convert("LEETCODEISHIRING", 4))
# LDREOEIIECIHNTSG
print(t.convert("ABC", 2))  # ACB
print(t.convert("ABCDEF", 5))  # ABCDFE
print(t.convert("ABCDE", 5))  # ABCDE
print(t.convert("A", 1))
print(t.convert("heltfchqssrwqgwanggkjlsownsdpoowubszfzratjwlpuldarnmehcbvuemiulcxdedcxfygbjyyxby"
                "qqmvxoyukchszuxwxdbbagzjklhiikiyavvzltwwyfqxzpvwszxvfzerknbuxkszhoaujwqhbjecycyrbyoizu"
                "cjhddgpxfynftxelehulktnkkqkaajucsdgxjvvoukvphzamjvxtomfacqaezwhuzntkkqagbvxkxywgtvbjjijnylsajzw", 742))

