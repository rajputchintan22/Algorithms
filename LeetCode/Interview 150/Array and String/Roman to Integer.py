class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map ={'I':1, 'V':5, 'X':10, 'L':50,'C':100,'D':500,'M':1000}
        number = 0
        if len(s) == 1:
            return symbol_map[s]
        for i in range(len(s)-1):
            if symbol_map[s[i]] < symbol_map[s[i+1]]:
                number -= symbol_map[s[i]]
            else:
                number += symbol_map[s[i]]
        number += symbol_map[s[-1]]
        return number




        