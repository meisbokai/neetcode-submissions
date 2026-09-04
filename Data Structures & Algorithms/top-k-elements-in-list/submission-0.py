class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #  each key is frequency, value is number
        count = {}
        freq = {}

        for n in nums:
            if n not in count:
                count[n] = 1
                if 1 not in freq:
                    freq[1] = {n}
                else:
                    freq[1].add(n)
            else:
                count[n] += 1
                freq[count[n]-1].remove(n)

                if count[n] not in freq: 
                    freq[count[n]] = {n}
                else:
                    freq[count[n]].add(n)

            # print(count)
            # print(freq)

        answer = [num for s in freq.values() for num in s][-k:]
        # print(answer)
        return answer
        
            