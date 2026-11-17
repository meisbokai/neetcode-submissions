"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_count = 0
        count = 0 

        starts = []
        ends = []

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        s = 0
        e = 0
        while s<len(starts) and e < len(ends):
            start = starts[s]
            end = ends[e]

            if start<end:
                count += 1
                max_count = max(count, max_count)
            
                s += 1
            else:
                count -= 1
                e += 1

        return max_count
        