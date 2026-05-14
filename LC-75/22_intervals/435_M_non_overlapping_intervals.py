class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1. sort the intervals array, so it first sorts on left bound
        2. if overlapping (right bound of previous overlaps with left bound of new)
            take the one that has a smaller right bound (to minimize overlap)
        """
        intervals.sort()
        sol = 0
        for i in range(1, len(intervals)):
            prev_right = intervals[i-1][1]
            curr_left = intervals[i][0]
            if prev_right > curr_left: # overlap
                # overwrite current with one with smaller right bound
                # only really need to overwrite if prev has smaller right bound
                curr_right = intervals[i][1]
                if prev_right < curr_right: 
                    intervals[i] = intervals[i-1]
                sol += 1
        return sol