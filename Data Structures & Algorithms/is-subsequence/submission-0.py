class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        for ch in s:
            if ch in t:
                continue
            else:
                return False