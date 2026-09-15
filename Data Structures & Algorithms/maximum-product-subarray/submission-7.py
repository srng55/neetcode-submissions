class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            current = nums[i]

            choices = [current, current * cur_max, current * cur_min]

            cur_min = min(choices)
            cur_max = max(choices)

            ans = max(ans, cur_max)

        return ans