class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sMap = Counter(s1)
        curMap = defaultdict(int)
        L = 0
        for R in range(len(s2)):
            curMap[s2[R]] += 1
            while (R - L + 1) > len(s1):
                if s2[L] in curMap:
                    curMap[s2[L]] -= 1
                    if curMap[s2[L]] == 0:
                        del curMap[s2[L]]
                L += 1
            if (R- L + 1) == len(s1) and curMap == sMap:
                return True
        return False
            