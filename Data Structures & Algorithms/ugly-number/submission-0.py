class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for p in [2,3,5]:
            while n % p == 0:
                n = n//p #double slash is integer division 
        return n == 1
        
        
