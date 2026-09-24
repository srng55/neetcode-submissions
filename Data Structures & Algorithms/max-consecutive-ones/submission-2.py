class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_1=0
        for num in nums:
            if num==1:
                count+=1
            else:
                max_1=max(max_1,count)

        return max_1
        