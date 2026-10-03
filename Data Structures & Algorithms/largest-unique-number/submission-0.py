class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num in unique:
                unique.remove(num)
            else:
                unique.add(num)
        return -1 if len(unique) == 0 else max(unique)