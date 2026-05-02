class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        IDEA: 
            use backtracking (recursion)
            1. call on backtrack(index = 0, curr = "")
                where 0 represents the index of the current digit we're exploring
            2. inside backtrack:
                i. check if we reach the end (if len(digits) == curr_string)
                    if so we append the current string to the solution
                ii. otherwise we load mapping[digits[digit_index]]
                    where mapping == characters possible using digits[i] (2 = abc)
        """
        self.m = {
            '2':"abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        self.n_digits = len(digits)
        self.digits = digits
        self.sols = []
        
        def backtrack(digits_index, curr):
            if len(curr) == self.n_digits:
                self.sols.append(curr)
                return
            else:
                items = self.m[self.digits[digits_index]]
                for item in items:
                    backtrack(digits_index + 1, curr+item)
        backtrack(0, "")
        return self.sols
