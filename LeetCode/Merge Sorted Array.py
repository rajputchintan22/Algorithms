class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        # Initialize a pointer for the last position of nums1
        k = m + n - 1

        # Iterate backwards through nums1 and nums2
        while i >= 0 and j >= 0:
            # Compare the current elements of nums1 and nums2
            # and place the larger one at the end of nums1
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements are left in nums2, place them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


            

        