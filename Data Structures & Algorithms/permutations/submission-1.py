class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        permutation=[]

        def backtrack():
            if len(permutation)==len(nums):
                res.append(permutation.copy())
                return

            for i in range(len(nums)):
                if nums[i] in permutation:
                    continue

                permutation.append(nums[i])
                backtrack()
                permutation.pop()

        backtrack()
        return res
        