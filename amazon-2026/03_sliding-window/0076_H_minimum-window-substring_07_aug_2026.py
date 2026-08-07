class Solution:
    def minWindow(self, s: str, t: str) -> str:
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