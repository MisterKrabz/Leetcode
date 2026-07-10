class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        
        # Stage 1: find the insert position 
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        
        # Stage 2: find overlapping intervals 
        start = i
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Stage 3: replace overlapping intervals with the merged interval. Use slicing instead of pop for faster time complexity. 
        intervals[start:i] = [newInterval]
        
        return intervals
