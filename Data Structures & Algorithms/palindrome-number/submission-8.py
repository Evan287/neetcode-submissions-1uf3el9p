class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        text = str(x)
        l, r = 0, len(text) - 1

        while l < r:
            if text[l] != text[r]:
                return False
                break
            else:
                l += 1
                r -= 1
        return True

