class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) <= 1:
            return True 
        max_jump = 1
        ans = True
        for i in range(len(nums)-2,-1,-1):
            if max_jump <= nums[i]:
                ans = True
                max_jump = 1
            else:
                ans = False
                max_jump += 1
        return ans

        