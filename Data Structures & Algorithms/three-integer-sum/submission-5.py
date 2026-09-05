class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        # if smallest element is non-negative, return empty list
        if nums[0] > 0:
            return []

        answers = set()

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1

            while j < k:
                if -nums[i] == nums[j] + nums[k]:
                    answers.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif -nums[i] > nums[j] + nums[k]:
                    j += 1
                else:
                    k -= 1

        # print(answers)

        return [list(t) for t in answers]


        