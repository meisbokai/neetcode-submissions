"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        print(intervals)
        intervals.sort(key=lambda s: s.start)
        print(intervals)

        end = 0
        for i in intervals:
            if i.start < end:
                return False
            end = i.end

        return True
