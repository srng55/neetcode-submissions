class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d={}

        for i in range(len(numbers)):
            comp=target-numbers[i]     

            if comp in d:
                return[d[comp]+1,i+1]

            d[numbers[i]] =i 