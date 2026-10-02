class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        sorted_queries=sorted(queries)

        heap = []
        res = {}
        i = 0

        for query in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= query:

                start,end = intervals[i]
                heapq.heappush(heap,(end-start+1,end))
                i+=1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                res[query] = heap[0][0]

            else:
                res[query] = -1

        return [res[query] for query in queries]


        