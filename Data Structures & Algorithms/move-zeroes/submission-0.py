class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        countZero = 0
        #Moving non zeroes to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l] = nums[i]
                l += 1
            else:
                countZero += 1
        #Add zeroes to the end
        for i in range(countZero):
            nums[(len(nums) -1) - i] = 0
         
        
        