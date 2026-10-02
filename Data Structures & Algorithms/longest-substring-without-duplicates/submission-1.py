class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        L = 0
        unique = set()
        for R in range(len(s)):
            while s[R] in unique and L < R:
                length = max(length, len(unique))
                unique.remove(s[L])
                L += 1
            unique.add(s[R])
            length = max(length, len(unique))
        return length