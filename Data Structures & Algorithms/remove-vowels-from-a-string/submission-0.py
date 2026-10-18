class Solution:
    def removeVowels(self, s: str) -> str:
        res = ""
        vowels = {
            "a": 0,
            "e": 0,
            "i": 0,
            "o":0,
            "u": 0
        }
        for i in range(len(s)):
            if s[i] not in vowels:
                res += s[i]
        return res