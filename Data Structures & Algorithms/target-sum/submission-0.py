class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def _findTargetSumWays(i, current_sum, memo):
            key = (i, current_sum)

            if key in memo:
                return memo[key]

            if i == len(nums):
                if current_sum == target:
                    return 1

                return 0

            add = _findTargetSumWays(i+1, current_sum + nums[i], memo)
            
            subtract = _findTargetSumWays(i+1, current_sum - nums[i], memo)

            memo[key] = add + subtract
            
            return memo[key]

        return _findTargetSumWays(0,0,{})
        