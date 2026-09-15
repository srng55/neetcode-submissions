class Solution:
    def rob(self, nums: List[int]) -> int:

        def _rob(nums,i,memo):

            if i in memo:
                return memo[i]

            if i>=len(nums):
                return 0

            rob = nums[i] + _rob(nums, i+2, memo)
            skip =_rob(nums, i+1, memo)

            memo[i] = max(skip,rob)

            return memo[i]

        if len(nums)==1:
            return nums[0]

        first = _rob(nums[1:], 0, {})
        second = _rob(nums[:-1], 0, {})

        return max(first,second)