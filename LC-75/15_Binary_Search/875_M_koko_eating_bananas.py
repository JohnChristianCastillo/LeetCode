class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        n Banana piles == |piles| = n
        h = time limit (in hours)

        tempo == k == bananas/hour

        find a 'k' s.t. all bananas are eaten within h hours
        
        IDEA:
        1. find max element of list: this is our upper bound
        2. BFS l,r: 1, upper_bound to find the minimum k
        - simulate the midpoint by going through the list
        
        """

        upper = max(piles)
        curr_min = upper

        l,r = 1, upper

        while l <= r:
            mid = l + (r-l)//2 # rate of which we will eat the bananas
            
            # simulate:
            hours_taken = 0
            for b in piles:
                hours_taken += ceil(b/mid)
                
            # now we check if this is a valid solution
            if hours_taken <= h:
                # we know we have enough room to maybe lessen the solution
                # --> move the right pointer to the left (mid)
                curr_min = min(curr_min, mid)
                r = mid - 1
            elif hours_taken > h:
                # rate is too low, move l higher
                l = mid + 1
        
        return curr_min
                