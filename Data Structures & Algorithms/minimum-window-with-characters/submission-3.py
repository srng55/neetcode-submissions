class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need={}

        for ch in t:
            need[ch]=need.get(ch,0)+1

        count={}
        l=0
        formed=0
        ans=""

        for r,ch in enumerate(s):
            count[ch]=count.get(ch,0)+1

            if ch in need and count[ch]==need[ch]:
                formed+=1

            while formed==len(need):
                if ans=="" or r-l+1 < len(ans):
                    ans=s[l:r+1]

                count[s[l]]-=1
                if s[l] in need and count[s[l]] < need[s[l]]:
                    formed-=1
                l+=1

        return ans 

       