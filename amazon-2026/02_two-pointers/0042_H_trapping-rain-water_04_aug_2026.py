class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height)-1
        max_l, max_r = height[l], height[r]
        # important since current l or r can be moved relative to the current value
        # even though their maximum value is larger than their current value
        # say 800047
        #     L   R   -> rmax should be 7 but r was moved cause it's still smaller than 8 
        max_vol = 0

        while l < r:
            left_turn = max_l <= max_r
            # turn defines which pointer will be moved inside
            # we move the smaller inside always

            if left_turn:
                max_vol += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                max_vol += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])
        
        return max_vol