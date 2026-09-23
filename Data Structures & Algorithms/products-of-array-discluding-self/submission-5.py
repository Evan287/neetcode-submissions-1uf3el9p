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
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[1])
            elif i == len(nums) -1:
                res.append(prefix[-2])
            else:
                res.append(postfix[i + 1] * prefix[i - 1])
        return res


        
        
