class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # array is structured in a way where the next element is the amount of
        # altitude you GAIN relative to previous position
        # use prefix sum list (summing left to right, saving each result)
        # then find the maximum value
        curr_max = 0
        prev = curr_max  # simulate having 0 as 1st element of prefix list
        for i in range(len(gain)):
            prefix_sum = prev + gain[i]
            prev = prefix_sum # use on next iteration
            gain[i] = prefix_sum
            curr_max = max(curr_max, prefix_sum)
        return curr_max