class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def _wordBreak(s, wordDict, i, memo):

            if i in memo:
                return memo[i]

            if i == len(s):
                return True

            for word in wordDict:
                if s[i :i + len(word)] == word:
                    if _wordBreak(s, wordDict, i+len(word), memo):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False

        return _wordBreak(s, wordDict, 0 ,{})
        