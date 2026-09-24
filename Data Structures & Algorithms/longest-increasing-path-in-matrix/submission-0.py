class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(r,c,memo):
            key = (r,c)

            if key in memo:
                return memo[key]

            longest = 1

            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue

                if matrix[nr][nc] <= matrix[r][c]:
                    continue

                length = 1 + dfs(nr, nc, memo)

                longest = max(longest, length)

            memo[key] = longest
            return memo[key]

        ans = 0

        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r, c, {} ))

        return ans 
        