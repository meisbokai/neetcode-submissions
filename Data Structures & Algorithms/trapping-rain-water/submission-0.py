class Solution:
    def trap(self, height: List[int]) -> int:
        lMax, rMax, left, right = 0, 0, 0, len(height) - 1
        area = 0
        
        while left < right:
            if height[left] < height[right]:
                lMax = max(lMax, height[left])
                area += (lMax - height[left])
                left += 1
            else:
                rMax = max(rMax, height[right])
                area += (rMax - height[right])
                right -= 1
        
        return area