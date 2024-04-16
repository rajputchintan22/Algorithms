class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)
        candies = [1] * n 
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)
            
print(Solution().candy([29,51,87,87,72,12]))