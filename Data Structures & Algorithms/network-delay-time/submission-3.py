class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [ [] for _ in range(n+1) ]

        for u,v,w in times:
            graph[u].append((v,w))

        
        shortest_time = [float("inf")] * (n+1)
        shortest_time[k] = 0

        minHeap =[(0,k)]

        while minHeap:

            time,node = heapq.heappop(minHeap)

            if time > shortest_time[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = new_time

                    heapq.heappush(minHeap, (new_time, neighbor))

        max_time = max(shortest_time[1:])

        if max_time == float("inf"):
            return -1

        else:
            return max_time                            