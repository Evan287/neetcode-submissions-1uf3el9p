class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = length = 0
        k = 0
        for R in range(len(nums)):
            #Check if number is 0
            if nums[R] == 0:
                k += 1
            if k > 1:
                if nums[L] == 0:
                    k -= 1
                L += 1
            length = max(length, R - L + 1)
        return length
                #Then increment k
            # if k is > 1:
                # calculate length, shift L