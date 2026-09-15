class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]
        candidates.sort()

        def backtrack(i,total):
            if total == target:
                res.append(sol.copy())
                return

            if i >= len(candidates) or total > target:
                return

            #pick
            sol.append(candidates[i])
            backtrack(i+1,total + candidates[i])
            
            #undo
            sol.pop()

            #skip duplicates
            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1

            #dont pick
            backtrack(i+1,total)

        backtrack(0,0)
        return res
        