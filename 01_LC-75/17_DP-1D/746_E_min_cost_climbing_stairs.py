class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        idea:
            have a cache to save the MINIMUM, amount of steps it takes to get to stair_i
            --> can be done in O(1) space using the cost list as cache
            min_stair_i = min(stair_i-1, stair_i-2)
        """
        cost.append(0) # last entry representing the minimum cost to reach the top of stair
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        
        return cost[-1]