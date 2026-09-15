class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def _change(amount, coins, i, memo):
            key=(amount,i)

            if key in memo:
                return memo[key]

            if amount == 0:
                return 1

            if i == len(coins):
                return 0

            total_ways = 0
            coin = coins[i]

            for qty in range(0, amount//coin + 1):
                remainder = amount - qty * coin

                total_ways += _change(remainder, coins, i+1, memo)

            memo[key] = total_ways
            return memo[key]

        return _change(amount, coins, 0, {})