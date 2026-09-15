class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct=[]
        count={}
        for s in arr:
            count[s]=count.get(s,0)+1
        for s in arr:
            if count[s]==1:
                distinct.append(s)
        
        return distinct[k-1] if len(distinct)>=k else ""


        