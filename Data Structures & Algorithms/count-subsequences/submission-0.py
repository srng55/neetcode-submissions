class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def dfs(i, j, memo):

            key = (i, j)

            if key in memo:
                return memo[key]
                
            if j == len(t):
                return 1

            if i == len(s):
                return 0


            if s[i] == t[j]:

                use = dfs(i+1, j+1, memo)
                skip = dfs(i+1, j, memo)

                memo[key] = use + skip
            else:
                skip = dfs(i+1, j, memo)

                memo[key] = skip

            return memo[key]

        return dfs(0,0,{})