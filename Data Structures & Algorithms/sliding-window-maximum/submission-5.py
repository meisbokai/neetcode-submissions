class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        # use max heap
        heap = []
        answer = []

        # store both idx and number
        for i in range(k):
            heap.append((nums[i], i))
        heapq.heapify_max(heap)

        # add first max
        answer.append(heap[0][0])

        for i in range(k, len(nums)):
            # check if max idx is still within window
            while heap[0][1] <= i-k:
                heapq.heappop_max(heap)
                if len(heap) == 0:
                    break
            
            heapq.heappush_max(heap, (nums[i], i))
            answer.append(heap[0][0])


        return answer