class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:x[1])

        count = 0
        realEnd = intervals[0][1]

        for start, end in intervals[1:]:

            if start < realEnd:
                count +=1
                realEnd = min(realEnd, end)

            else:
                realEnd = end

        return count