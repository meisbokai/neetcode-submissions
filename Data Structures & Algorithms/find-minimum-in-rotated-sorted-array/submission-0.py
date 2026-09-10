class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated sorted array -> still sorted from start of rotation
        # i.e. at any point, if nums[i+1] < nums[i], nums[i+1] is the minimum

        # binary search
        left, right = 0, len(nums) - 1  
        
        while left < right:
            mid = left + (right - left) // 2

            # if mid > right, search right
            if nums[mid] > nums[right]:
                left = mid + 1
            else: # else search left
                right = mid
                
        # left == right
        return nums[left]

   

        