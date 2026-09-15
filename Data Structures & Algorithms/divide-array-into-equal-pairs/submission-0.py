class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d={}
        pairs=len(nums)//2
        pair=0
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]-=1
                del d[num]
                pair+=1

        return pair==pairs 
            


        