class Solution:
    def longestCommonPrefix(self, strs) -> str:
        list_string = [list(s) for s in strs]
        common_part = list_string[0]
        for i in strs[1:]:
            temp = []
            for j in range(min(len(common_part),len(i))):
                if i[j] == common_part[j]:
                    temp.append(i[j])
                else:
                    break
            common_part = temp
        return "".join(common_part)
        