class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVal = -1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            maxVal = max(maxVal, height*width)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxVal

        