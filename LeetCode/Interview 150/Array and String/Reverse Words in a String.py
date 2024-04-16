class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(" ")
        ans = []
        for i in range(len(str_list)-1,-1,-1):
            if str_list[i] != "":
                ans.append(str_list[i])
        return " ".join(ans)        