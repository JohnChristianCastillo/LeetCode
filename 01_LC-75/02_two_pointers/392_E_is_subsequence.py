class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        to avoid edge cases like below we just use two pointers
        if len(s) > len(t):
            return False
        if not s:
            return True
        for v in t:
            if s[i] == v:
                i += 1
        return len(s) == i 
        """
        
        i, j = 0, 0
        len_s = len(s)
        len_t = len(t)
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len_s