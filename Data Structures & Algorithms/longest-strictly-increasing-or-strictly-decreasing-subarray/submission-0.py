class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count=1
        for i,num in enumerate(nums):
            if i>0 and nums[i]>nums[i-1]:
                count+=1
                maxcount=max(maxcount,count)

            if i<len(nums) and nums[i]<nums[i+1]:
                count+=1
                maxcount=max(maxcount,count)

        return maxcount