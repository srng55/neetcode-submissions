class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        q = deque()
        fresh = 0

        def rotOrange(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            if (r, c) in visited:
                return

            if grid[r][c] != 1:
                return

            visited.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        time = 0

        while q and fresh > 0:

            for i in range(len(q)):

                r, c = q.popleft()

                rotOrange(r + 1, c)
                rotOrange(r - 1, c)
                rotOrange(r, c + 1)
                rotOrange(r, c - 1)

            time += 1

            # All newly added oranges are now rotten
            for r, c in q:
                grid[r][c] = 2

            fresh -= len(q)

        if fresh == 0:
            return time

        return -1

        