class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        nums=[]
        for row in grid:
            for num in row:
                nums.append(num)

        for num in nums:
            i=abs(num)-1

            if nums[i] < 0:
                repeated=abs(num)

            else:
                nums[i]=-nums[i]
        
        for i,num in enumerate(nums):
            if num>0:
                return [repeated,i+1]