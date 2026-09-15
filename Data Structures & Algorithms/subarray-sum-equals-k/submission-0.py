class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        total=0
        ans=0

        for num in nums:
            total+=num

            if total-k in prefix:
                ans+=prefix[total-k]

            prefix[total]=prefix.get(total,0)+1

        return ans


