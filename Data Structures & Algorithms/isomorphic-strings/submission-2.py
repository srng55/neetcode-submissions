class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d={}
        used=set()

        for ch1,ch2 in zip(s,t):

            if ch1 in d and d[ch1] != ch2:
                return False

            if ch2 in used and ch1 not in d:
                return False

            d[ch1]=ch2
            used.add(ch2)

        return True