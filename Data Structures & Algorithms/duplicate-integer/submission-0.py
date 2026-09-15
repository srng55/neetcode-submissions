class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        flag=0
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                return True
        return False