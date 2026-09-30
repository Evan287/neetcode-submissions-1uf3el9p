class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        #Two pass
        # First pass, everything to the left
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        #first pass * everything to the right
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = postfix * res[i]
            postfix *= nums[i]
        
        return res