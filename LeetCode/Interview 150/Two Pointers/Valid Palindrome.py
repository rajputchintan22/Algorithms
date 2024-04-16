class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_str = []
        for i in s:
            temp = ord(i)
            if temp > 64 and temp<91:
                stripped_str.append(chr(temp+32))
            elif temp > 96 and temp<123:
                stripped_str.append(i) 
            elif temp > 47 and temp<58:
                stripped_str.append(i)
        ns="".join(stripped_str)
        print(ns)
        i = 0
        j= len(ns)-1
        while i<j:
            if ns[i]==ns[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        