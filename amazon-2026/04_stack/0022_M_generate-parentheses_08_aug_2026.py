class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        def backtrack(open_brackets, close_brackets, comb):
            if len(comb) == 2*n:
                if open_brackets == n and close_brackets == n:
                    sol.append(comb)
                return
            if open_brackets < n:
                backtrack(open_brackets + 1, close_brackets, comb + '(')
            if close_brackets < open_brackets:
                backtrack(open_brackets, close_brackets + 1, comb + ')')
        backtrack(0, 0, "")
        return sol