class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        sol = 0
        for i, v in enumerate(s):
            # make sure no duplicate
            while v in seen:
                seen.remove(s[l])
                l += 1
            seen.add(v)
            sol = max(sol, len(seen))

        return sol
