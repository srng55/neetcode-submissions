class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0 :
            return False

        target = total // 2

        def _canPartition(i, target, memo):

            if target == 0:
                return True

            if i == len(nums) or target < 0:
                return False

            key = (i, target)

            if key in memo:
                return memo[key]

            pick = _canPartition(i+1, target-nums[i], memo)

            skip = _canPartition(i+1, target, memo)

            memo[key] = pick or skip

            return memo[key]

        return _canPartition(0, target, {}) 
        