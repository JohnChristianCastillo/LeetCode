class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        there are 3 options: buy, sell, skip
        we can use recursion + memoization
        -> we can afterwards extend to tabularization (bottom up iterative)
         self note: for DP problems, try go from:
        recursion -> recursion + memoization -> tabulation(bottom-up DP (filltable  backwards)) -> no table
        no table can only be the case if you se that each row only depends on the next row (that you solved firse)
        """
        n = len(prices)

        # -----------------------------
        # Create a 2D DP table manually
        # dp[i][1] = best profit from day i when you CAN buy
        # dp[i][0] = best profit from day i when you CANNOT buy (holding stock)
        # -----------------------------
        dp = []
        for i in range(n+1):
            dp.append([0, 0])   # dp[i] = [cannot_buy, can_buy]

        # Base case:
        # dp[n][0] = dp[n][1] = 0 already

        # Fill table backwards
        for i in range(n-1, -1, -1):
            # If you can buy at day i
            buy = -prices[i] + dp[i+1][0]   # buy stock
            # --> since you spend money to buy stock, your profit goes down buy prices[i]
            # --> after buying, your only possible state is dp[i+1][0] [next state, can't buy]
            skip_buy = dp[i+1][1]           # skip
            dp[i][1] = max(buy, skip_buy)

            # If you cannot buy (you are holding a stock)
            sell = prices[i] - fee + dp[i+1][1]  # sell stock
            skip_sell = dp[i+1][0]               # skip
            dp[i][0] = max(sell, skip_sell)

        return dp[0][1]
        # --> this can ultimately converted to constant space since we only really need to look at 1 step into the future

        """
        This can be converted to a bottom-up solution where instead of asking:
        “At day i, I look at the future and choose the best option.”
        we now ask:
        “Let’s fill in the answers for the future first,
        then walk backward so the answers are already waiting for us.”
        this just means we start from self.n then walk backwards

        
        self.prices = prices
        self.fee = fee
        self.n = len(prices)
        self.memo = {}
        def rec(idx, can_buy):
            if (idx, can_buy) in self.memo:
                return self.memo[(idx, can_buy)]
            if idx == self.n:
                return 0
            # posssibilities: buy, sell, skip
            buy, sell = float('-inf'), float('-inf')
            if can_buy:
                buy = -prices[idx] + rec(idx+1, False)
            else: # sell
                sell = prices[idx] - fee + rec(idx+1, True)
            # do nothing
            skip = rec(idx+1, can_buy)
            
            res = max(buy, sell, skip)
            self.memo[(idx, can_buy)] = res
            return res
        
        return rec(0, True)
        """