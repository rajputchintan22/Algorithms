class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zig_zag_list = [[] for _ in range(numRows)]
        inc_dec = 1
        row_ptr = 0
        max_row = numRows - 1
        for i in range(len(s)):
            zig_zag_list[row_ptr].append(s[i])
            if row_ptr == 0:
                inc_dec = 1
            elif row_ptr == max_row:
                inc_dec = -1
            row_ptr += inc_dec
        ans = ""
        for  i in zig_zag_list:
            ans += "".join(i)
        return ans


            