class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCount = Counter(magazine)
        ranCount = Counter(ransomNote)
        for i, n in ranCount.items():
            if magCount[i] < n:
                return False
        return True
            
