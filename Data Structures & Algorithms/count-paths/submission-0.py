class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def _uniquePaths(r,c,memo):

            pos=(r,c)

            if pos in memo:
                return memo[pos]

            if r >= m or c >= n:
                return 0

            if r == m-1 and c==n-1:
                return 1

            down_count = _uniquePaths(r+1, c, memo)       
            right_count = _uniquePaths(r, c+1, memo)

            memo[pos] = down_count + right_count

            return memo[pos]

        return _uniquePaths(0,0,{})   