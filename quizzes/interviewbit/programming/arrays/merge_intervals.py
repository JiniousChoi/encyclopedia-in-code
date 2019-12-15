#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if new_interval.start > new_interval.end:
            new_interval.start, new_interval.end = new_interval.end, new_interval.start
        non_overlap = []
        overlaps = []
        
        while intervals and (new_interval.end < intervals[-1].start):
            non_overlap.append(intervals.pop(-1))
        
        assert intervals==[] or (new_interval.end >= intervals[-1].start)
        while intervals and (intervals[-1].end >= new_interval.start):
            overlaps.append(intervals.pop(-1))
        assert intervals==[] or (intervals[-1].end < new_interval.start)
        
        if overlaps != []:
            new_interval.start = min(new_interval.start, overlaps[-1].start)
            new_interval.end = max(new_interval.end, overlaps[0].end)
        
        intervals.append(new_interval)
        while non_overlap:
            intervals.append(non_overlap.pop(-1))
        
        return intervals


import unittest


class SolutionTest(unittest.TestCase):
    def test_basics(self):
        pass


if __name__ == "__main__":

    unittest.main()
