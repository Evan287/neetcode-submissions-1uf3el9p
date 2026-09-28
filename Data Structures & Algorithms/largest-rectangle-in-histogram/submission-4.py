class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                #: width runs between the previous smaller bar (new top) and the next smaller bar (i)
                width = i if not stack else (i - stack[-1] - 1)
                maxArea = max(maxArea, height * width)
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else (n - stack[-1] - 1)
            maxArea = max(maxArea, height * width)
        
        return maxArea
