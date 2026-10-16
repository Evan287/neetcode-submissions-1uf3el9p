class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        numMap = Counter(nums)
        for num in numMap:
            if num +1 not in numMap and num - 1 not in numMap:
                return False
            if numMap[num] > 1:
                return False
        return True