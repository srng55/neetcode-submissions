class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l=0
        ans=float("inf")
        summ=0

        for r,ch in enumerate(nums):
            summ+=nums[r]

            while summ>=target:
                ans=min(ans,r-l+1)

                summ-=nums[l]
                l+=1

        if ans==float('inf'):
            return 0
        return ans



            
        