class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [], [None] * len(nums)
        preProduct, postProduct = 1, 1
        res = []
        for n in nums:
            preProduct *= n
            prefix.append(preProduct)
        for i in range(len(nums) - 1, -1, -1):
            postProduct *= nums[i]
            postfix[i] = postProduct
        for index, val in enumerate(nums):
            if index == 0:
                res.append(postfix[1])
            elif index == len(nums) -1:
                res.append(prefix[-2])
            else:
                res.append(postfix[index + 1] * prefix[index - 1])
        return res


        
        
