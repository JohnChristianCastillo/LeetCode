class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        need = [0]*26
        window = [0]*26

        if n2 < n1:
            return False

        # init windows up till s1 
        for i in range(n1):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        if need == window: return True

        # extend window and decrease it simultaneously (since window size can only really be len(s1))
        for r in range(n1, n2):
            window[ord(s2[r]) - ord('a')] += 1

            l = r-n1
            window[ord(s2[l]) - ord('a')] -= 1

            if need == window:
                return True

        return False