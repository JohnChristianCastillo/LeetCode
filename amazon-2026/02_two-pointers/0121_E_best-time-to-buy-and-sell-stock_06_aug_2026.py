class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 1
        if n == 0 or k == 0:
            return 0

        FLAT = 0        # we own no share right now
        HOLDING = 1     # we own exactly one share right now
        NEG = float('-inf')

        # ---- what the state means ---------------------------------------------
        # dp[i][j][s] = the most CASH we can be holding, given that:
        #
        #   i = how many days we have already lived through, 0..n
        #       i = 0 is a SENTINEL row meaning "before the market ever opened".
        #       Because of it, the price belonging to row i is prices[i-1], not
        #       prices[i]. That off-by-one is the price of a clean base case.
        #
        #   j = the CAP on how many buys we are allowed to have made, 0..k.
        #       "At most j", not exactly j. A buy spends one unit of cap;
        #       a sell is free. So a completed round trip costs 1.
        #
        #   s = FLAT or HOLDING.
        #
        # The value stored is CASH, and it is legitimately negative while HOLDING,
        # because buying subtracts the price. We only ever read a FLAT cell as the
        # answer, and by then we have sold, so the money is back.

        # ---- base case, pre-filled into every cell ----------------------------
        #   FLAT    ->    0 : nothing has happened yet, no profit.
        #   HOLDING -> -inf : impossible state. This forces every max() involving
        #                     it to reject it until a real buy overwrites it.
        #                     Seeding 0 here instead is THE classic bug - it claims
        #                     we are holding a share we never paid for.
        dp = []
        for i in range(n + 1):
            row = []
            for j in range(k + 1):
                row.append([0, NEG])        # [FLAT value, HOLDING value]
            dp.append(row)

        # Two families of cells are never written by the loops below, so they keep
        # that seed forever - and the seed happens to be exactly right:
        #   dp[0][j] -> the sentinel day.
        #   dp[i][0] -> a cap of zero buys: profit pinned at 0, holding impossible
        #               for all time. This is the floor the whole stack rests on.

        # ---- fill it in --------------------------------------------------------
        for i in range(1, n + 1):
            p = prices[i - 1]

            for j in range(1, k + 1):

                # end today FLAT: rest as we were, or sell the share we held.
                # Selling does not spend cap, so we stay on layer j.
                dp[i][j][FLAT] = max(dp[i-1][j][FLAT],
                                    dp[i-1][j][HOLDING] + p)

                # end today HOLDING: keep the share, or buy today.
                # Buying spends cap, so the FLAT we came from was operating under
                # the smaller cap j-1. This is the ONLY place two cap layers
                # ever talk to each other.
                dp[i][j][HOLDING] = max(dp[i-1][j][HOLDING],
                                        dp[i-1][j-1][FLAT] - p)

        # Every read above is dp[i-1][...], an index that cannot appear on the
        # left-hand side, so loop order is irrelevant. Nothing to reason about.

        # ---- the answer --------------------------------------------------------
        # Last day, full cap, owning nothing.
        # No max() over j is needed: resting is always an option, so the table is
        # non-decreasing in j - a bigger cap can simulate a smaller one by
        # declining to use it - and layer k already contains the shorter answers.
        # We read FLAT rather than HOLDING because ending the run still holding a
        # share means we spent money and never got it back. Never optimal.
        return dp[n][k][FLAT]