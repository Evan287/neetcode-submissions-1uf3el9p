from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = defaultdict(int)
        for num in nums:
            numMap[num] += 1
        return max(numMap, key=numMap.get)