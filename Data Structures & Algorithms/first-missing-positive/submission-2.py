class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        valid = False
        while valid == False:
            if i not in nums:
                valid = True
            else:
                i += 1
        return i
