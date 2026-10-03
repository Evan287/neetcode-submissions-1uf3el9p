class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {c:i for i, c in enumerate(nums2)}
        res = [0] * len(nums1)
        for i, n in enumerate(nums1):
            res[i] = count.get(n, 0)
        return res