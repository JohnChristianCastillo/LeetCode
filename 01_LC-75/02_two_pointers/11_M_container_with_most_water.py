class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1. use two pointers, one at each end
        2. every iteration:
            calculate current volume and update max volume
            ask: which pointer to move to possibly get more volume?
            --> ans: the shorter wall
        """

        l, r = 0, len(height)-1
        max_area = 0
        while l < r:
            l_height = height[l]
            r_height = height[r]
            curr_area = (r-l)*min(r_height, l_height)
            max_area = max(max_area, curr_area)

            # move pointers
            if r_height < l_height:
                r -= 1
            else:
                l += 1
        
        return max_area