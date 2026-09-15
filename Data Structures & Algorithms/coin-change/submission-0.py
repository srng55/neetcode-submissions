class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def _coinChange(coins,amount,memo):

            if amount in memo:
                return memo[amount]

            if amount == 0 :
                return 0

            if amount < 0:
                return float("inf")

            min_count = float("inf")

            for coin in coins:

                count = 1 + _coinChange(coins,amount-coin, memo)

                min_count = min(min_count, count)

            memo[amount]= min_count
            return memo[amount]

        result = _coinChange(coins,amount,{})

        if result == float("inf"):
            return -1

        return result

        