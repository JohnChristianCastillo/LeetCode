class Solution:
   def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)      # remaining need per char (goes negative once surplus)
        missing = len(t)      # total characters still needed
        l = 0
        start, end = 0, 0     # best window found (s[start:end])

        for r, ch in enumerate(s, 1):
            if cnt[ch] > 0:
                missing -= 1
            cnt[ch] -= 1

            if missing == 0:
                while cnt[s[l]] < 0:      # shrink past surplus chars
                    cnt[s[l]] += 1
                    l += 1
                if end == 0 or r - l < end - start:
                    start, end = l, r
                cnt[s[l]] += 1              # evict one required char
                missing += 1
                l += 1

        return s[start:end]

""" same concept, lazy Counter solution
        need = Counter(t)  # t's representation
        window = Counter()
        
        l = 0
        sol = ""

        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            
            # need - window: subtracts counts key by key, but keeps ONLY entries
            # where the result is strictly positive (need[k] - window[k] > 0);
            # any key where the result is zero or negative is dropped entirely.
            #
            # So need - window = "which characters I'm still short on, and by how much."
            # e.g. need={A:1,B:1,C:1}, window={A:1,B:1,C:1,D:2} -> need - window = {}
            #      need={A:1,B:1,C:1}, window={A:1,D:2}         -> need - window = {B:1, C:1}
            #
            # If window already has enough (or more) of every character need
            # requires, every difference is <= 0, so the result is an empty Counter.
            while not (need - window):
                if sol == "" or (r - l + 1) < len(sol):
                    sol = s[l:r+1]
                # shrink window and see if we can find better solution
                window[s[l]] -= 1
                l += 1
        return sol
"""