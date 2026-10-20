class Solution:
    def firstUniqChar(self, s: str) -> int:
        cMap = Counter(s)
        unique = -1
        for c, count in cMap.items():
            if count == 1:
                unique = c
                break
        for i, c in enumerate(s):
            if c == unique:
                unique = i
        return unique
