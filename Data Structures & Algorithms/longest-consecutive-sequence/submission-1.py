class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # early return
        if len(nums) <= 1:
            return len(nums)

        # convert to hash O(n)
        seen = {}
        for n in nums:
            seen[n] = 1

        # sort O(nlogn)
        # print(sorted(seen))

        prev = next(iter(sorted(seen, key=seen.get)))
        longest = 1
        cur_longest = 1
        for m in sorted(seen):
            # print(m, prev, cur_longest, longest)
            if m-prev == 1:
                prev = m
                cur_longest += 1
            else:
                prev = m
                if cur_longest > longest:
                    longest = cur_longest
                cur_longest = 1

        if cur_longest > longest:
            longest = cur_longest

        return longest
        