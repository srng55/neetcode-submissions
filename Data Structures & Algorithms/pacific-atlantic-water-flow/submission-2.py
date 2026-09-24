class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def explore(r, c, visited):

            visited.add((r, c))

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue

                if (nr, nc) in visited:
                    continue

                if heights[nr][nc] < heights[r][c]:
                    continue

                explore(nr, nc, visited)

        for r in range(rows):
            explore(r, 0, pacific)
            explore(r, cols - 1, atlantic)

        for c in range(cols):
            explore(0, c, pacific)
            explore(rows - 1, c, atlantic)

        ans = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans