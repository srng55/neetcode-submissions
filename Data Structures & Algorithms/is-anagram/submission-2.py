class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d={}

        if len(s)!=len(t):
            return False

        for ch in s:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]+=1

        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch]-=1

            if d[ch]==0:
                del d[ch]

        if len(d)==0:
            return True
        else:
            return False

        