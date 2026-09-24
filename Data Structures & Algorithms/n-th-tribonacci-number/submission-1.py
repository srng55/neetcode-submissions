class Solution:
    def tribonacci(self, n: int) -> int:

        def _tribonacci(n):

            if n==0:
                return 0

            if n==1 or n==2:
                return 1


            return _tribonacci(n-1) + _tribonacci(n-2) + _tribonacci(n-3)
        
        return _tribonacci(n)