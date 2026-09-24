class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        for i in range(1,len(nums)):
            if len(nums)==1:
                return True

            if not (nums[i]%2==0 and nums[i-1]%2==1) or (nums[i]%2==1 and nums[i-1]%2==0):
                return False

        return True


        