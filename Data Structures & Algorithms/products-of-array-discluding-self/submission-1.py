class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer = [1] * len(nums)

        # # O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(answer)):
        #         if i!=j:
        #             answer[i] *= nums[j] 
        # print(answer)


        # return answer

        # Keep results
        answer = [1] * (len(nums)+2)
        left = [1] * (len(nums)+2)
        right = [1] * (len(nums)+2)

        # Left (O(N))
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            left[i+1] = prod
        # print(left)

        # Right (O(N))
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            prod *= nums[i]
            right[i+1] = prod
        # print(right)

        # prod (O(N))
        for i in range(1, len(answer)-1):
            answer[i] = left[i-1] * right[i+1]
        # print(answer)


        return answer[1:len(answer)-1]
