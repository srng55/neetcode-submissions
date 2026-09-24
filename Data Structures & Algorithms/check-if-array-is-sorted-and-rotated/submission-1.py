class Solution:
    def check(self, nums: List[int]) -> bool:

        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]-1 or nums[i] != len(nums)+1:
                return False

        return True 


        