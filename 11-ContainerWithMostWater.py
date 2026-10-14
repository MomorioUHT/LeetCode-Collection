class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        
        left,right = 0,len(height)-1
        maxArea = 0
        
        while (left < right):
            currArea = min(height[left], height[right]) * (right-left)
            maxArea = max(currArea, maxArea)
        
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
                
        return maxArea