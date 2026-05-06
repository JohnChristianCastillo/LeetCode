class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        1. Opearion(s) allowed: delete()
                text1=   c   a   b   d     let's fill out row 1
                    0    0   0   0   0 
                    ===================
                b   0 || 0   0   0   0   

        text2   d   0 || 0   0   0   0  
        --------------------------------
                text1=   c   a   b   d   RULE 1: when a char matches, take the value of the substrings before them(prev diagonal), then add 1
                    0    0   0   0   0    so for "cab and b" : b matches so we take the value of: "ca and '' " -> prev diagonal = 0
                    ===================
                b   0 || 0   0   1   0   

        text2   d   0 || 0   0   0   0    Now let's try on: cab + bd !!!
        --------------------------------------------------------------
                text1=   c   a   b   d   RULE 2: if characters don't match, we take the maximum match we've had so far: (either top or left)
                    0    0   0   0   0    --> looking at cab + bd --> d and b does not match BUT cab + b did 
                    ===================     => left of cab + bd: ca + bd = 0 |
                b   0 || 0   0   1   0      => top of cab + bd: cab + b = 1  |=> max(0,1) = 1
        text2   d   0 || 0   0   1       
        --------------------------------------------------------------
                text1=   c   a   b   d    now let's look at the whole strings: cabD + bd
                    0    0   0   0   0    RULE 1 again: since d and d matches: we look at the substrings before them and get their maximum match 
                    ===================     we then add 1 to that since D matches ==> max(cab + b) + 1 = 1 + 1 = 2
                b   0 || 0   0   1   0      
        text2   d   0 || 0   0   1   2    

        ALGO:
        1. construct our 2D matrix (notice size = +1 to get correct structure)
        2. loop over the constructed matrix and initialize their values
        3. return last element of matrix 
        """

        dp = []
        l1 = len(text1)
        l2 = len(text2)
        for r in range(l2+1):  # notice I used text2 to act as the rows to match the example
            dp.append([0]*(l1+1))

        for r in range(1, len(dp)):
            t2 =  text2[r-1]
            for c in range(1, len(dp[0])):
                t1 = text1[c-1]
                if t1 == t2:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    top = dp[r-1][c]
                    left = dp[r][c-1]
                    dp[r][c] = max(top,left)
        return dp[l2][l1]