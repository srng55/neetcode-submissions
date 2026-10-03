class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        minHeap = [(0, src, 0)]

        visited = set()

        while minHeap:
            cost, city, stops = heapq.heappop(minHeap)

            if city == dst:
                return cost

            if stops > k:
                continue

            if (city, stops) in visited:
                continue

            visited.add( (city,stops) )

            for neighbor, price in graph[city]:
                new_cost = cost + price

                heapq.heappush(minHeap, (new_cost, neighbor, stops+1))


        return -1