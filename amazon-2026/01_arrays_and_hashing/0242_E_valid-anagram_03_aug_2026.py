class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram must have
        # 1. same length
        # 2. same characters

        m1 = Counter(s)
        m2 = Counter(t)
        return m1 == m2