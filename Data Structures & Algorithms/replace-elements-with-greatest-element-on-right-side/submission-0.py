class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = -1
        res = [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            res[i] = maxVal
            maxVal = max(maxVal, arr[i])
        return res
        