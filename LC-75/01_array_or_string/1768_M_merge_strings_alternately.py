class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0,0
        l1, l2 = len(word1), len(word2)
        sol = ""
        while i < l1 and j < l2:
            sol += word1[i] + word2[j]
            i += 1
            j += 1
    
        if i < l1:
            sol += word1[i:]
        else:
            sol += word2[j:]
        return sol

