class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] and nums[i]<nums[i+1]:
                continue
            else:
                return False
                

            if nums[i]<nums[i-1] and nums[i]>nums[i+1]:
                coninue
            else:
                return False
        return True
        