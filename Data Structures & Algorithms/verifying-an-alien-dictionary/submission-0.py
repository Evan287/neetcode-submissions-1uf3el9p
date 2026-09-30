class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            for c1, c2 in zip(words[i], words[i+1]):
                if order.index(c1) > order.index(c2):
                    return False
                elif order.index(c1) < order.index(c2):
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return False
        return True

