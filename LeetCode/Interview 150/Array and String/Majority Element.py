class Solution:
    def majorityElement(self, nums) -> int:
        dic = {}
        n = len(nums)
        for i in nums:
            if i in dic:
                dic[i] -= 1
                if dic[i] == 0:
                    return i
            else:
                dic[i] = n//2
        return nums[0]
#also

        # nums.sort()
        # idx = len(nums) // 2
        # return nums[idx]