class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc=True
        dec=True
        for i in range(len(nums)):
            if nums[i]>nums[i+1]:
                inc=False
            if nums[i]<nums[i+1]:
                dec=False

        return dec or inc            
        