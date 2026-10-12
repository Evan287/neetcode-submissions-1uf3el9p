class Solution:
    def findLucky(self, arr: List[int]) -> int:
        numMap = Counter(arr)
        maxLucky = 0
        for num in numMap:
            if numMap[num] == num:
                maxLucky = max(maxLucky, num)
        return maxLucky if maxLucky != 0 else - 1