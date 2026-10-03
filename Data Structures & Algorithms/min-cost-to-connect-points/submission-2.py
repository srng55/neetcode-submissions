class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        minHeap = [(0,0)]
        visited = set()

        total_cost = 0

        while minHeap:

            #point -> index
            cost, point = heapq.heappop(minHeap)

            if point in visited:
                continue

            visited.add(point)
            total_cost += cost

            x1, y1 = points[point]

            for neighbor in range(len(points)):
                if neighbor in visited:
                    continue

                x2,y2 = points[neighbor]

                distance = abs(x1-x2) + abs(y1-y2)

                heapq.heappush(minHeap, (distance, neighbor))

        return total_cost
        