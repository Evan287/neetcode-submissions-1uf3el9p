class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Three Pass 
        #First Pass: Turn Negatives into zero
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        #Second Pass: Mark values (1, n) that are seen
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1
        #Third Pass: Find first positive int
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1