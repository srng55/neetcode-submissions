class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows=len(grid)
        cols=len(grid[0])
        maxArea=0
        visited=set()

        def explore(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return 0
            
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            area=1

            area+=explore(r+1,c)
            area+=explore(r-1,c)
            area+=explore(r,c+1)
            area+=explore(r,c-1)

            return area


        for r in range(rows):
            for c in range(cols):

                if grid[r][c]== 1 :
                    area = explore(r,c)
                    maxArea=max(maxArea,area)

        return maxArea
        