class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      sorted_s = sorted(s)
      sorted_t = sorted(t)
      print(sorted_s)
      print(sorted_t)
      for i in range (0, len(sorted_s)):
        if len(sorted_s) != len(sorted_t):
                return False
        if sorted_s[i] != sorted_t[i]:
                return False
      return True