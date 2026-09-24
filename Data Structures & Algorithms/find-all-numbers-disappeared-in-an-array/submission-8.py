class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            i=abs(num)
            nums[i]=-abs(nums[i])

        for i,num in enumerate(nums):
            if num>0:
                res.append(i)

        return res

        