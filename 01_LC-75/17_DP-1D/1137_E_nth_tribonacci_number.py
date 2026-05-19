class Solution:
    def __init__(self):
        self.cache = {
            0: 0,
            1: 1,
            2: 1
        }
    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        else:
            sol = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            self.cache[n] = sol
            return sol
    
            