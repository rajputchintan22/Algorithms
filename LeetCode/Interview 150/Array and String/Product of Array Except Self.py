class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        flag = 0
        for i in nums:
            if i == 0 and flag == 0:
                flag = 1
            else:
                prod *= i
        for i in range(0,len(nums)):
            if nums[i] != 0 and flag == 1:
                nums[i] = 0
            elif nums[i] != 0 and flag == 0:
                nums[i] = prod//nums[i]
            else:
                nums[i]=prod
        return nums