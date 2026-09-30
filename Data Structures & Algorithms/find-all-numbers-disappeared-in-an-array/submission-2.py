class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i + 1 not in nums:
                res.append(i+1)
        return res