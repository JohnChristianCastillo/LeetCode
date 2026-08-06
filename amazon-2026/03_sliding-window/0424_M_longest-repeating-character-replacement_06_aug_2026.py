class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        reframe: A window is valid if (window length) - (count of the most frequent character in the window) <= k
        use map to keep track of frequency

        """
        freqs = {}
        max_freq = 0
        l = 0   # we move this right if we exceed k to decrease the window
        max_window = 0

        for r, v in enumerate(s):
            """
            1. increment count of v and update if max_freq has increased
            2. see if it exceeds, if so, move l inward
            3. calculate new max_window
            """
            freqs[v] = freqs.get(v, 0) + 1
            max_freq = max(max_freq, freqs[v])

            if (r - l + 1) - max_freq > k:
                # (r - l + 1) is the current window length.
                # window_length - max_freq = how many chars in the window are "not the majority char",
                # i.e. how many replacements this window would need.
                # If that exceeds k, the window is invalid -> shrink from the left.
                freqs[s[l]] -= 1    # remove s[l] from the frequency count since it's leaving the window
                l += 1              # move the left edge forward, shrinking the window by one

            max_window = max(max_window, r - l + 1)
        
        return max_window