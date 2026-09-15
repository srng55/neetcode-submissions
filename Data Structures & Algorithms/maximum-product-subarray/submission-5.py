class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def _maxProduct(nums, i, memo):
            if i in memo:
                return memo[i]

            if i==0:
                return (nums[0],nums[0])

            prev_max,prev_min = _maxProduct(nums, i-1, memo)

            current=nums[i]

            choices=[current, current * prev_max, current * prev_min ]

            max_product = max(choices)
            min_product = min(choices)

            memo[i] = (max_product, min_product)

            return memo[i]

        memo = {}
        answer = float("-inf")

        for i in range(len(nums)):
            max_product, min_product = _maxProduct(nums, i, memo)
            answer = max(answer, max_product)

        return answer  
