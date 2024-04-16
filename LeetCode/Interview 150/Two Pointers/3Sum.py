class Solution:
    def threeSum(self, nums):
        ans = []
        if len(nums) < 3:
            return ans
        nums.sort()
        n = len(nums)
        print(nums)
        for k in range(0,n-2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            if nums[k] > 0 :
                break
            i = k+1
            j = n-1
            while i<j:
                temp = nums[k] + nums[i] + nums[j]
                if temp == 0:
                    ans.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while j > 0 and nums[j] == nums[j+1]:
                        j -= 1
                    while i < n and nums[i] == nums[i-1]:
                        i += 1
                elif temp > 0:
                    j -= 1
                    while j > 0 and nums[j] == nums[j+1]:
                        j -= 1 
                else:
                    i += 1
                    while i < n and nums[i] == nums[i-1]:
                        i += 1
        return ans




        