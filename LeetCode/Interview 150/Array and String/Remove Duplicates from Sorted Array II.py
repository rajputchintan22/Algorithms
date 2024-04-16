
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        unique_index = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]
                if i+1 <= len(nums)-1:
                    if nums[i] == nums[i+1]:
                        nums[unique_index+1] = nums[i]
                        unique_index += 1
                unique_index += 1
            elif i==2 and nums[i] == nums[i-1] and nums[i-2] != nums[i]:
                unique_index += 1
        return unique_index
