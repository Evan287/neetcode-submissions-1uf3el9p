class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sMap = Counter(s)
        res = []
        for c in order:
            if c in sMap:
                res.extend(c *sMap[c])
        
        ordMap = Counter(order)
        for c in sMap:
            if c not in ordMap:
                res.extend(c * sMap[c])
        
        return ''.join(res)