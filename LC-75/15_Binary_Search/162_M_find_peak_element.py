class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        idea:
            use binary search
            cases:
                if left and right are smaller: SOL FOUND!
                elif left is LARGER:
                    then we pursue that larger side
                    - since current is smaller than left, we're most likely to find a peak there
                elif right is larger:
                    pursue the right side (same as above)
                    effectively: left = mid, right = current right bound
                
        """
        n = len(nums)
        l,r = 0, n-1
        while l <= r:
            mid = l + (r-l)//2
            curr = nums[mid]
            left = nums[mid - 1] if mid -1 >= 0 else float("-inf")
            right = nums[mid + 1] if mid+1 < n else float("-inf")

            # case 1: peak found
            if  curr > left and curr > right:
                return mid
            # case 2: left side is rising, so peak must be on left
            elif curr <= left: # left can be a peak and curr can be its right smaller element
                # [... LEFT, mid, right] (we ditch right side )
                r = mid-1
            # case 3: right side is rising, peak must be on the right
            else:
                l = mid + 1
        
        return -1