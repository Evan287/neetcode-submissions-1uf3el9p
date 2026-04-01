class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (0, len(nums) -1):
            leftPtr = nums[i]
            rightPtr = nums[i + 1]
            if nums and leftPtr == rightPtr:
                return True
        return False