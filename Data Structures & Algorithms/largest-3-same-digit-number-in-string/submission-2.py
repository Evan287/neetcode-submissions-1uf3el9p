class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxGoodInt = "0"
        for i in range(len(num) - 2):
            if num[i] == num[i+1] and num[i +1 ] == num[i + 2]:
                maxGoodInt = max(maxGoodInt, num[i: i+3])
        return "" if maxGoodInt == "0" else maxGoodInt