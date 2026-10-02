class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newStart = newInterval[0]
        newEnd = newInterval[1]

        res=[]

        for start,end in intervals:

            if start > newEnd:

                res.append([newStart,newEnd])

                newStart = start
                newEnd = end

            elif newStart > end:

                res.append([start,end])

            else:

                newStart = min(newStart, start)
                newEnd = max(newEnd, end)

        res.append([newStart,newEnd])

        return res

        

