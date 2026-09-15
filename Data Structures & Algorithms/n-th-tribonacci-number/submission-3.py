class Solution:
    def tribonacci(self, n: int) -> int:

        def _tribonacci(n,memo):

            if n in memo:
                return memo[n]

            if n==0:
                return 0

            if n==1 or n==2:
                return 1


            memo[n] =  _tribonacci(n-1,memo) + _tribonacci(n-2,memo) + _tribonacci(n-3,memo)
            return memo[n]
        
        return _tribonacci(n,{})