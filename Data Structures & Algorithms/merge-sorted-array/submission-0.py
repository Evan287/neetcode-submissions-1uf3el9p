class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
      #nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2
        l = 0
        for i in range(m, len(nums1)):
            if nums1[i] == 0:
                nums1[i] = nums2[l]
                l += 1
        nums1.sort()
