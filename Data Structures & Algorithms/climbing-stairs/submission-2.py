class Solution:
    def climbStairs(self, n) -> int:

        def _climbStairs(n,memo) :

            if n==0:
                return 1

            if n<0:
                return 0

            if n in memo:
                return memo[n]

            memo[n] = _climbStairs(n-1,memo) + _climbStairs(n-2,memo)

            return memo[n]


        return _climbStairs(n,{})

