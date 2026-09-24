class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        max_int=0x0FFFFFFF

        while b:
            carry=(a&b)<<1
            a=(a^b) & mask
            b=carry & mask

        return a
