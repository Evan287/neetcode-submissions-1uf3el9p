class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countRed = 0
        countWhite = 0
        countBlue = 0
        #First pass: Count each color
        for num in nums:
            if num == 0:
                countRed += 1
            elif num == 1:
                countWhite += 1
            else:
                countBlue += 1
        #Second pass, overwrite each index
        i = 0
        while countRed > 0 and i < len(nums):
            nums[i] = 0
            i += 1
            countRed -= 1
        while countWhite > 0 and i < len(nums):
            print(countWhite)
            nums[i] = 1
            i += 1
            countWhite -= 1
        while countBlue > 0 and i < len(nums):
            nums[i] = 2
            i += 1
            countBlue -= 1
