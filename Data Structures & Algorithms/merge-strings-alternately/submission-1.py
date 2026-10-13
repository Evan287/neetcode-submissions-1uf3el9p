class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        start = min(len(word1), len(word2))
        for c1, c2 in zip(word1, word2):
            res += c1 + c2
        if len(word1) > len(word2):
            res += word1[start:]
        elif len(word2) > len(word1):
            res += word2[start:]
        return res
        