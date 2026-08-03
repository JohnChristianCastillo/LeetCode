class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [v.lower() for v in s if v.isalnum()]
        s = "".join(s)

        return s == s[::-1]