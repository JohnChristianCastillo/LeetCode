class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        1. sum until k elements
        2. loop from i = k 
        3. return avg
        do not AVERAGE (divide) during the pass, do it on return
        """

        curr_sum = sum(nums[0:k])
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum -= nums[i-k]
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum/k