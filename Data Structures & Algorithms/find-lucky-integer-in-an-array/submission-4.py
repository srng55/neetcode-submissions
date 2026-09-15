class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count={}
        ans=[]
        maxi=0
        for num in arr:
            count[num]=count.get(num,0)+1

        for num in arr:
            if count[num]==num:
                ans.append(num)
                
        return max(ans) if ans else -1
    
    