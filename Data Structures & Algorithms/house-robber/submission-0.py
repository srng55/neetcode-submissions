class Solution:
    def rob(self, nums: List[int]) -> int:
         def _rob(nums,i,memo):
            if i in memo:
                return memo[i]

            if i>=len(nums):
                return 0

            rob = nums[i] + _rob(nums, i + 2, memo)

            skip = _rob(nums, i + 1, memo)

            memo[i] = max(rob, skip)

            return memo[i]


         return _rob(nums, 0, {})