class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ=nums[i]
        for i in rnage(1,len(nums)):
            if nums[i] > nums[i-1]:
                summ+=nums[i]

            else:
                summ=nums[i]

        return summ
        