class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tMap = Counter(t)
        window = defaultdict(int)
        need, have = len(tMap), 0
        L = 0
        res, resLen = [-1, -1], float("inf")
        for R in range(len(s)):
            c = s[R]
            window[c] += 1

            if c in tMap and window[c] == tMap[c]:
                have += 1
            
            while have == need:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = R-L+1

                window[s[L]] -= 1
                if s[L] in tMap and window[s[L]] < tMap[s[L]]:
                    have -= 1
                L += 1

        L, R = res
        return s[L: R + 1] if resLen != float("inf") else ""