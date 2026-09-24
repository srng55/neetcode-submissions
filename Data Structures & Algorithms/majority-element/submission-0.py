class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        res=[]
        for num in nums:
            count[num]=count.get(num,0)+1
            
            if count[num] > (n/2):
                res.append(num)
        return res