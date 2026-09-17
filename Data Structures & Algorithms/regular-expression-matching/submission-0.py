class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i, j, memo):
            key = (i,j)

            if key in memo:
                return memo[key]

            if j == len(p):
                return i == len(s)
            
            match = ( i < len(s) and ( s[i]==p[j] or p[j]==".") )

            if j+1 < len(p) and p[j+1] == "*":
                skip = dfs(i, j+2, memo)
                use = False
                
                if match:
                    use = dfs(i+1, j, memo)

                memo[key] = skip or use

            else:

                if match:
                    memo[key] = dfs(i+1, j+1, memo)

                else:
                    memo[key] = False

            return memo[key]

        return dfs(0,0,{})