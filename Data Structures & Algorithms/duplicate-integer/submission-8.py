class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = set()
        for num in nums:
            if num not in prev:
                prev.add(num)
            else:
                return True
        return False