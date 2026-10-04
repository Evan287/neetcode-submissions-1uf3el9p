class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L, countOnes, res = 0, 0, 0
        for R in range(len(nums)):
            if nums[R] == 1:
                countOnes += 1
            while (R - L + 1) - countOnes > k:
                if nums[L] == 1:
                    countOnes -= 1
                L += 1
            res = max(res, R - L + 1)
        return res