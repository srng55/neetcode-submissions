class Solution:
    def getSum(self, a: int, b: int) -> int:
        a=bin(a)[2:]
        b=bin(b)[2:]

        return a|b