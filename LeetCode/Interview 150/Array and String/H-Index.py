class Solution:
    def hIndex(self, citations) -> int:
        citations.sort()
        ans = 0
        n = len(citations)
        for i in range(len(citations)):
            remaining = n-i
            ans = max(ans,min(citations[i],remaining))
        return ans

print(Solution().hIndex([1,3,1]))