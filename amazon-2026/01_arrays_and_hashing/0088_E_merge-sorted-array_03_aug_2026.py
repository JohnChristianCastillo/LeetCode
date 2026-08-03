class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        idea: 
        1. lists are sorted SO
        - we fill nums1 from back to front
        -- constantly asking ourselved "which of the 2 back elements of the two lists is larger?"
        """

        last_pos = len(nums1) - 1
        n1, n2 = m-1, n-1
        while n1 >= 0 and n2 >= 0:
            # find out who's larger and place it at current pos
            if nums1[n1] >= nums2[n2]:
                nums1[last_pos] = nums1[n1]
                n1 -= 1
            else:
                nums1[last_pos] = nums2[n2]
                n2 -= 1
            last_pos -= 1
        
        # possible nums2 still has elements
        while n2 >= 0:
            nums1[last_pos] = nums2[n2]
            n2 -= 1
            last_pos -= 1