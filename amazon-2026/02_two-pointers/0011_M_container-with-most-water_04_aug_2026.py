class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        idea:
        two pointers

        the limiting factor is the smallest balk, so move that inside and update max area
        
        """

        l, r = 0, len(height) - 1
        max_vol = 0
        while l < r:
            min_height = min(height[l], height[r])
            width = r-l
            vol = min_height*width
            max_vol = max(max_vol, vol)

            # update pointer
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return max_vol

