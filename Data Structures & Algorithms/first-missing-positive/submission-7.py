class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in count:
                return i
        return i + 1