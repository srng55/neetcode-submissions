class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        res=[]
        sol=[]

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            #Dont pick number
            backtrack(i+1)

            #pick number
            sol.append(nums[i])
            backtrack(i+1)

            #undo
            sol.pop()

        backtrack(0)
        return res
        