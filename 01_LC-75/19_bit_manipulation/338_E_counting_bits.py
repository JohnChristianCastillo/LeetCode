class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = []
        cache = {}
        while n >= 0:
            # print(cache)
            t = n
            if t in cache:
                sol.append(cache[t])
                n -= 1
                continue
            bits = 0
            while t > 0:
                bits += t & 1
                t = t // 2
            cache[n] = bits # use n here as key since t = 0 now
            sol.append(bits)
            n -= 1
        return sol[::-1]

        