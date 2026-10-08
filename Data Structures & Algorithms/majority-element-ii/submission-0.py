class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numMap = Counter(nums)
        res =[]
        for n in numMap:
            if numMap[n] > (len(nums)//3): #3
                res.append(n)
        return res
