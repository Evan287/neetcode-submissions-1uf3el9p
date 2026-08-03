class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t) or len(s) > len(t):
            return False

        sortS =  "".join(sorted(s))
        sortT =  "".join(sorted(t))

        for i in range(0, len(sortS)):
            if sortS[i] != sortT[i]:
                return False
        return True