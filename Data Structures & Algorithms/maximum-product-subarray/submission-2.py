class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def _maxProduct(nums, i, memo):
            if i in memo:
                return memo[i]

            if i==0:
                return (nums[0],nums[0],nums[0])

            prev_max, prev_min, ans = _maxProduct(nums, i-1, memo)

            current=nums[i]

            choices=[current, current * prev_max, current * prev_min ]

            max_product = max(choices)
            min_product = min(choices)

            ans = max(max_product, ans)

            memo[i] = (max_product, min_product, ans)

            return memo[i]

        _,_,ans = _maxProduct(nums,len(nums)-1,{}) 

        return ans