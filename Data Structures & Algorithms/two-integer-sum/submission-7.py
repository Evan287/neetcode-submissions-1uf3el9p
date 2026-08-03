class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums:
                j = nums.index(diff)
                if i != j:
                    if i < j:
                        return [i, j]
                    else:
                        return [j, i]