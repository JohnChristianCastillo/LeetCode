class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        you need to find 2 things
        1. total product without the 0's (since 0 makes product = 0)
        2. how many 0's there are (if more than 1 then all product = 0)
        """

        zeros = 0
        product = 1
        for v in nums:
            if not v:
                zeros += 1
            else:
                product *= v
        
        for i, v in enumerate(nums):
            if not v:
                # zero unless there's another zero
                if zeros <= 1:
                    nums[i] = product
                else:
                    nums[i] = 0
            else: # v is not zero
                if zeros: # if there exist zeros then this will become zero
                    nums[i] = 0
                else:
                    nums[i] = product//v
        
        return nums