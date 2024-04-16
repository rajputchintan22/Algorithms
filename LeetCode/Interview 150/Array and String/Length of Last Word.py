class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pointer  = len(s)-1
        while s[pointer] == ' ':
            pointer -= 1
        count = 0
        while pointer>=0 and s[pointer] != ' ':
            pointer -= 1
            count += 1
        return count