class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def _maxProfit(i, can_buy, memo):
            key = (i, can_buy)

            if key in memo:
                return memo[key]

            if i >= len(prices):
                return 0

            if can_buy:
                buy = -prices[i] + _maxProfit(i+1, False, memo)
                skip = _maxProfit(i+1, True, memo)

                memo[key] = max(buy,skip)

            else:
                sell = prices[i] + _maxProfit(i+2, True, memo)
                skip = _maxProfit(i+1, False, memo)

                memo[key] = max(sell,skip)

            return memo[key]

        return _maxProfit(0,True,{})
        