class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        prefix = 0
        sums = [0] * len(nums)
        res = [0] * len(nums)
        #Build Prefix sum 
        for i in range(len(nums)):
            prefix += nums[i]
            sums[i] = prefix
        
        #Build array with largest score at each index
        for i in range(len(sums)):
            if i == 0:
                res[i] = sums[i]
            elif i == len(sums) - 1:
                res[i] = sums[i] if sums[i] > nums[-1] else nums[-1]
            else:
                if sums[i] > (sums[-1] - sums[i - 1]):
                    res[i] = sums[i]
                else:
                    res[i] = (sums[-1] - sums[i - 1])
        return max(res)
        #Prefix 5, -4, 2
        #Suffix
        #First check is the prefix sum at the current in
        #Second check is the last prefix sum minus the prefix sum to the left of i 

