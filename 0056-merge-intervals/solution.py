class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []

        for start, end in intervals:
            if not ret or ret[-1][1] < start:
                ret.append([start, end])
            else:
                ret[-1][1] = max(ret[-1][1], end)

        return ret
