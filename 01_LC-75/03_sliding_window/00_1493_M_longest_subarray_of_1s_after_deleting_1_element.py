class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        sliding window + coversion limit = 1
        """
        l = 0
        k = 1
        ones = 0
        maxx = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            ones += 1

            # If we exceeded allowed zeros, shrink
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
                ones -= 1

            maxx = max(maxx, ones)

        return maxx - 1
