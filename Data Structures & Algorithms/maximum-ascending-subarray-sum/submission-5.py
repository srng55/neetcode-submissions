class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ=nums[0]
        maxsum=0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                summ+=nums[i]
                maxsum=max(maxsum,summ)

            else:
                summ=nums[i]
                maxsum=max(maxsum,summ)

        return summ
        