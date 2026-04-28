class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
        K sessions
        hire 1 worker per session
        each session we consider the first |candidates| and the last |candidates|
        """

        # idea: have 2 heaps: 1 for the 1st |candidates|, 1 for the last |candidates|
        len_costs = len(costs)
        if k >= len_costs:
            return sum(costs) # base case, we want to hire more than available

        l,r = 0, len_costs-1

        h1, h2 = [], []
        while l < candidates:
            heapq.heappush(h1, costs[l])
            l += 1
        
        
        while len_costs - r <= candidates and l <= r:
            heapq.heappush(h2, costs[r])
            r -= 1

        # start the sessions
        total_costs = 0
        while k > 0:
            # if h2 is empty we just default add h1
            if not h2 or (h1 and h1[0] <= h2[0]):
                # <= since index also matters and h1 has lower index than h2
                total_costs += heapq.heappop(h1)
                # add new element to h1 if we can
                if l <= r:
                    heapq.heappush(h1, costs[l])
                    l += 1
            else:
                total_costs += heapq.heappop(h2)
                if r >= l:
                    heapq.heappush(h2, costs[r])
                    r -= 1
            k -= 1

        return total_costs