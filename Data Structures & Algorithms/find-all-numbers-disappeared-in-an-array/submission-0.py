class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(1,len(nums)):
            if i not in nums:
                res.append(i)
        
        return res
        