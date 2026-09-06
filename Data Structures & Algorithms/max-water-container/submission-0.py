class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # i.e. max product between (j-i) and min(height[i],heigh[j])
        max_vol = 0

        l = 0
        r = len(heights)-1
        while l < r:
            vol = (r-l) * min(heights[l], heights[r])
            max_vol = max(vol, max_vol)
            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1

        return max_vol


        