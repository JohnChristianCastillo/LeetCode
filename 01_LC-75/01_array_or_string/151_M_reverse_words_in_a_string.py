class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        s = ""
        while words:
            s += words.pop() + " "

        return s[:-1] # pop the last space