class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def dfs(i, j, memo):

            key = (i, j)

            if key in memo:
                return memo[key]

            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:

                memo[key] = dfs(i+1, j+1, memo)

            else:
                delete = dfs(i+1, j, memo)
                insert = dfs(i, j+1, memo)
                replace = dfs(i+1, j+1, memo)

                memo[key] = 1 + min(delete, insert, replace)
            
            return memo[key]

        return dfs(0,0,{})