class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        stackIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= stackIntervals[len(stackIntervals)-1][1]:
                stackIntervals[len(stackIntervals)-1][1] = max(stackIntervals[len(stackIntervals)-1][1], intervals[i][1])
            else:
                stackIntervals.append(intervals[i])
        return stackIntervals
