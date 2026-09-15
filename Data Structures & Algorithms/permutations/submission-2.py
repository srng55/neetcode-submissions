class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]

        def backtrack():
            if len(sol)==len(nums):
                res.append(sol.copy())
                return

            for num in nums:
                #dont pick
                if num in sol:
                    continue
                #pick
                sol.append(num)
                backtrack()
                #undo
                sol.pop()

        backtrack()
        return res
        