class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        idea: use tabulation where upperleft diagonal is 
                    H   O   R   S   E
            0   0   1   2   3   4   5  # from empty string to HORSE
            R   1   1   2   2   3   4
            O   2   2   1   2   3   4
            S   3   2   2   2   2   3
            if same: take upper left diagonal
            it not same take the minimum number of edit + 1 
            -> edit == delete, insert, replace
            - delete: top: since going top means we decrease our src by 1
            - insert: left: since from the left's perspective we inserted 
            - replae: top left diagonal
        IMPORTANT: 
        the notion of insert/delete is relative to which string is the src
        and which is the target
        for us we're using 
            string2(ROS) as source, and string1(HORSE)as target
        """

        # init table
        rows = len(word2)
        cols = len(word1)
        dp = []
        for row in range(rows+1):
            dp.append([0]*(cols+1))
        # initialize first row that goes from empty string to HORSE (cols)
        for col in range(cols+1):
            dp[0][col] = col
        # init first column that goes from empty string to ROS (rows)
        for row in range(rows+1):
            dp[row][0] = row

        # fill out table according to edit formula:
        # if same letters = take topleft diag
        # if not: min(top,left,diag)+1
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                left = dp[row][col-1]   # insert (because from left's perspective, you inserted a new letter)
                top = dp[row-1][col]    # delete (because )
                diag = dp[row-1][col-1] # replace or match
                if word2[row-1] == word1[col-1]:
                    dp[row][col] = diag
                else:
                    dp[row][col] = min(top, left, diag) + 1

        return dp[rows][cols]        