class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        use two pointers
        keep extending r until you are forced to move L
        --> happens when you don't have k anymore
        """
        
        l, r = 0, 0
        max_ones = 0
        curr_ones = 0
        zero_count = 0
        while r < len(nums):
            if nums[r] == 0:
                zero_count += 1
            curr_ones += 1
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                curr_ones -= 1
                l += 1

            r += 1
            max_ones = max(max_ones, curr_ones)

        return max_ones

        