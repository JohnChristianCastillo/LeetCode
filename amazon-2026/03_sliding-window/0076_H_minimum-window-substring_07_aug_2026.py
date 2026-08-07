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