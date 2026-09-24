class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count={}
        for num in arr:
            count[num]=count.get(num,0)+1

        for num in arr:
            if count[num]==num:
                return num
        
        return -1