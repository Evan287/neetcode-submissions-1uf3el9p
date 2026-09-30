class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = [1] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]

        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        for i, n in enumerate(nums):
            if i == 0:
                res[i] = postfix[i + 1]
            elif i == len(nums) -1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        return res