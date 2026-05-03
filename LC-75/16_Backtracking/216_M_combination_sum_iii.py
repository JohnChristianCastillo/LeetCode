class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        k = amount of digits you can and have to use
        digits = 1 through 9, for each solution each digit can only be used once
        n = target sum
        
        idea:
            use backtracking function S.T. 'backtrack(curr_digit, digits_used, curr_sum)'
            where 
                curr_digit: our anchor, so we know which digits to iterate next
                digits_used (list): list of digits used, to check on whether we used K digits
                    - use list to easily append to our solutions list
                curr_sum: current sum of the used digits 

            ALGO:
                create backtrack()
                    - check if solution is found
                    - if not:
                        call backtrack continuing from current digit
        """
        self.sols = []
        def backtrack(curr_digit: int, digits_used: list, curr_sum: int):
            if len(digits_used) == k:
                if curr_sum == n:
                    self.sols.append(digits_used)
                return
            
            for i in range(curr_digit, 10):
                backtrack(i+1, digits_used + [i], curr_sum + i)

        backtrack(1, [], 0)

        return self.sols
           
            



        