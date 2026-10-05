"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(meetings)):
            if meetings[i].start < meetings[i - 1].end:
                return False
        return True