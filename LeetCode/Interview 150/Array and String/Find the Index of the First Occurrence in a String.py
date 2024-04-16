class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length_of_needle = len(needle)
        length_of_heystack = len(haystack)
        if length_of_needle>length_of_heystack:
            return -1
        elif length_of_heystack == length_of_needle:
            if needle == haystack:
                return 0
            else:
                return -1
        i = 0
        while i < length_of_heystack-length_of_needle + 1:
            print(i)
            if haystack[i] == needle[0]:
                if i + length_of_needle <= length_of_heystack:
                    k = length_of_needle-1
                    while k >= 0:
                        if k == 0:
                            return i
                        if needle[k] == haystack[i+k]:
                            k -= 1
                        else:
                            break
                        
                else:
                    return -1
            i += 1
        return -1
                            
print(Solution().strStr(
   haystack= "abc", needle= "c"
))

