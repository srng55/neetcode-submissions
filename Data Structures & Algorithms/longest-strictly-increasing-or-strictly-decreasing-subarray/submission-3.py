class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=0
        dec=0
        ans=0

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc+=1
                dec=1
            elif nums[i]<nums[i-1]:
                dec+=1
                inc=1

            else:
                inc=1
                dec=1
            
            ans=max(ans,dec,inc)

        return ans
