class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows=len(grid)
        cols=len(grid[0])
        count=0
        visited=set()

        def explore(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return

            if (r,c) in visited:
                return
            
            if grid[r][c]=="0":
                return

            visited.add((r,c))

            explore(r+1,c)
            explore(r-1,c)
            explore(r,c+1)
            explore(r,c-1)



        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count+=1
                    explore(r,c)  

        return count     