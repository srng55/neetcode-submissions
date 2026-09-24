class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i=0

        for ch in t:
            if i < len(s) and ch==s[i]:
                i+=1

        return len(s)-i