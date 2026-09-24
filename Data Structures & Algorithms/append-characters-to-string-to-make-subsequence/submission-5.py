class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i=0

        for ch in s:
            if i < len(t) and ch==s[i]:
                i+=1

        return len(t)-i