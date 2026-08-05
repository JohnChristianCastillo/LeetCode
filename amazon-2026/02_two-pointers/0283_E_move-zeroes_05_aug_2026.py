class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        reframe the question:
        1. move all non 0 to the front
        """
        insert_pos = 0
        for i, v in enumerate(nums):
            if v:
                tmp = v
                nums[i] = 0
                nums[insert_pos] = tmp
                insert_pos += 1
        
        return nums