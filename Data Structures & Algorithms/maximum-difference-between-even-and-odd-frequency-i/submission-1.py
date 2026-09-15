class Solution:
    def maxDifference(self, s: str) -> int:
        count={}

        for ch in s:
            count[ch]=count.get(ch,0)+1

        odd=0
        even=float('inf')

        for count in count.values():

            if count%2==0:
                even = min (even, count)

            else:
                odd = max (odd,count)

        return odd-even

        



        