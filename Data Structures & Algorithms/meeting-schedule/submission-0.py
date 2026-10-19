"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # for i in intervals:
        #     print(i.start, i.end)


        asc = sorted(intervals, key=lambda i: i.start)

        cur_time = -1

        for i in asc:
            if cur_time > i.start:
                return False
            cur_time = i.end
            # print(i.start, i.end)

        return True
