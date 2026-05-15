class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        balloon pops when arrow's x = [x_s, x_e]
        return: minimum arrows that must be shot to burst all balloons

        Idea:
            1. sort points so we can find overlaps
            2. if a no overlap == new section == new arrow
                we update prev_end to the new current end 
                and increase the arrows we need
            3. if overlap: WE TAKE THE MINIMUM ENDPOINT
                we always carry over the overlap from the smaller endpoint 
                [x1 x2 x3]
                    [y1 y2 y3] => 
                if we take y3 and new previous then we might find a balloon 
                range S.T. we cant pop the x balloons, so take min(X3,Y3) as prev_end
        """
        groups = 1
        points.sort()
        prev_end = points[0][1] 
        for i in range(1, len(points)):
            curr_start, curr_end = points[i]
            # check for overlap
            if curr_start <= prev_end: 
                # take the endpoint which is minimal
                prev_end = min(prev_end, curr_end)
            else: # no overlap! new arrow!
                groups += 1
                prev_end = curr_end
        
        return groups