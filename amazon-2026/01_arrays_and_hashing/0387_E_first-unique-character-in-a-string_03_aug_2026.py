class Solution:
    def firstUniqChar(self, s: str) -> int:
        ctr = Counter(s)
        for i, c in enumerate(s):
            if ctr[c] == 1:
                return i
        return -1