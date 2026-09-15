class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def _minCostClimbingStairs(cost,i,memo):

            if i in memo:
                return memo[i]

            if i>=len(cost):
                return 0

            one = cost[i] + _minCostClimbingStairs(cost,i+1,memo)
            two = cost[i] + _minCostClimbingStairs(cost,i+2,memo)

            memo[i] = min(one,two)

            return memo[i]

        return min  (
                    _minCostClimbingStairs(cost,0,{}),
                    _minCostClimbingStairs(cost,1,{})
                    )