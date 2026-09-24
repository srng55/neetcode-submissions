class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i=0

        for ch in t:
            if i < len(t) and ch==t[i]:
                i+=1

        return len(t)-i