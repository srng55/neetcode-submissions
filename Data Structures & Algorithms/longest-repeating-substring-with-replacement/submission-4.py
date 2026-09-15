class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count={}
        l=0
        maxFreq=0
        ans=0

        for r,ch in enumerate(s):
            count[ch]=count.get(ch,0)+1
            maxFreq=max(maxFreq,count[ch])

            window=r-l+1

            while window - maxFreq > k:
                count[s[l]]-=1
                l+=1

                window=r-l+1

            ans=max(ans,window)

        return ans
