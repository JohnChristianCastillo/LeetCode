class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        reframe the question:
        whenever you encounter a non 0, move it to the front
        -->
        1. use two pointer:
            l = 0 spot where you can swap a non 0 element
            r = scanner 
        """

        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                # find a new l s.t. nums[l] = 0
                """but this is just l + 1 since
                1. if nums[l+1] != 0 BEFORE SWAP:
                    then this was originally r
                    which is now back to 0
                2. if nums[l+1] == 0:
                    r skipped this to find a non 0
                    which mean l+1 is a good spot
                """
                l += 1
            r += 1

