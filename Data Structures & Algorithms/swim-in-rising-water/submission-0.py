class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        minHeap = [ (grid[0][0], 0, 0) ]
        visited = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while minHeap:
            time, row, col = heapq.heappop(minHeap)

            if (row,col) in visited:
                continue

            visited.add((row,col))

            if row == len(grid)-1 and col == len(grid[0])-1:
                return time

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if nr < 0 or nr >= len(grid):
                    continue

                if nc < 0 or nc >= len(grid[0]):
                    continue

                if (nr,nc) in visited:
                    continue

                new_time = max(time, grid[nr][nc])

                heapq.heappush(minHeap, (new_time, nr, nc))