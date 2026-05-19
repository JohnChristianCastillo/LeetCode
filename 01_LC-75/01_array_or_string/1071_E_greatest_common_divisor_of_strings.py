class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        there can only be a gcd of str1 and str2 iff:
        str1 + str2 == str2 + str1

        and their gcd string is from any of the two strings
        UNTIL the GCD of their lengths
        """
        def _gcd(a, b):
            # The Euclidean Algorithm is based on this fact:
            # gcd(a, b) == gcd(b, a % b)
            #
            # Why?
            # Because the GCD of two numbers does NOT change if you replace
            # the larger number with its remainder when divided by the smaller one.
            #
            # Example:
            # gcd(48, 18) == gcd(18, 48 % 18 == 12)
            #
            # Each step makes the numbers smaller, so the loop always terminates.
            while b != 0:
                # At each iteration:
                # 'a' becomes the previous 'b'
                # 'b' becomes the remainder of a % b
                #
                # This moves us closer to the base case where b == 0.
                #
                # When b becomes 0, 'a' holds the GCD.
                a, b = b, a % b
            return a

        res = ""
        if str1 + str2 == str2 + str1:
            return str1[:_gcd(len(str1),len(str2))]
        return res