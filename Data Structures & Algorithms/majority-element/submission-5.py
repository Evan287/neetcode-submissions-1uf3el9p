class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore Voting algorithm

        res = count = 0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res