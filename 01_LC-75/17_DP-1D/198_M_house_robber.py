class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            idea:
        start from index 2, modify in place whether it's best to NOT rob it, or rob it together with the n-2 entry  
        """
        if len(nums) == 1:
            return nums[0]  # special case
        nums[1] = max(nums[0], nums[1]) # initialize i=1 correctly
        for i in range(2, len(nums)):   
            # take sum of now and n-2 or take previous largest
            # important for case like [2,1,1,2] where sol = 4      
            nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        print(nums)
        return nums[-1]