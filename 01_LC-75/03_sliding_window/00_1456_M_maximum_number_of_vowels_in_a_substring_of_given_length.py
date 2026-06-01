class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')  # s is all lowercase

        max_vowels = 0
        curr_vowels = 0
        for i, c in enumerate(s):
            # check if we have a vowel
            # check if we exceeded k
            # -- if so remove left most letter
            # update max vowels
            if c in vowels:
                curr_vowels += 1
            if i >= k:
                if s[i-k] in vowels:
                    curr_vowels -= 1
            max_vowels = max(max_vowels, curr_vowels)
        
        return max_vowels
            

