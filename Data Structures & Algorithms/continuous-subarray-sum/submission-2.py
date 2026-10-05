class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0
        for i,n in enumerate(nums):
            total += n
            mod = total % k
            if mod not in remainder:
                remainder[mod] = i
            #Calculate length is >= 2
            elif i - remainder[mod] >= 2:
                return True
        return False