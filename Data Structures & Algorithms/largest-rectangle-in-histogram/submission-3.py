class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        heights.append(0)
        
        for i,h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                idx=stack.pop()
                height=heights[idx]

                left=stack[-1] if stack else -1
                right=i

                width=right-left-1
                area=width*height

                maxArea=max(maxArea,area)
            
            stack.append(i)

        return maxArea