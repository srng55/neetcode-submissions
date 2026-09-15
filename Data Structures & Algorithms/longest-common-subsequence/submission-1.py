class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def _longestCommonSubsequence(text1, text2, i, j, memo):
            key = (i,j)

            if key in memo:
                return memo[key]

            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                memo[key] = 1 + _longestCommonSubsequence(text1,text2,i+1,j+1,memo)

            else:
                skip_i = _longestCommonSubsequence(text1, text2, i+1, j, memo)
                skip_j = _longestCommonSubsequence(text1, text2, i, j+1, memo)

                memo[key] = max(skip_i,skip_j)
            return memo[key]

        return _longestCommonSubsequence(text1,text2,0,0,{})