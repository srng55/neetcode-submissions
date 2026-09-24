class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        def dfs(left, right, memo):
            key = (left,right)

            if key in memo:
                return memo[key]

            if left + 1 == right:
                return 0

            coins = 0

            for x in range(left + 1, right):

                current = ( 
                    nums[left] * nums[x] * nums[right]
                    + dfs(x, right, memo)
                    + dfs(left, x, memo)
                    ) 
                
                coins = max(coins, current)

            memo[key] = coins
            return memo[key]

        return dfs(0, len(nums)-1, {})