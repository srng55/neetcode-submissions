class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            i=num-1
            nums[i]=-nums[i]

        for i,num in enumerate(nums):
            if num>0:
                res.append(i+1)

        return res

        