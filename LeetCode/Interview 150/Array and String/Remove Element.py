class Solution:
    def removeElement(self, nums, val: int) -> int:
        count = 0
        last_index = len(nums)-1
        if last_index == -1:
            return 0
        while nums[last_index] == val:
            nums[last_index] = '_'
            count += 1
            last_index -= 1
        i = 0
        while i <= last_index:
            if nums[i] == val:
                nums[i] = nums[last_index]
                nums[last_index] = val
                while nums[last_index] == val:
                    nums[last_index] = '_'
                    count += 1
                    last_index -= 1
                i += 1
            else:
                i += 1
        return len(nums)-count
    

    def removeElement2(self, nums, val: int) -> int:
        nums[:] = [i for i in nums if i!=val]