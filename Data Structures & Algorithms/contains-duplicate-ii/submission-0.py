class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        seen=set()

        for r,ch in enumerate(nums):
            if ch in seen:
                return True

            seen.add(ch)

            if r-l+1>k:
                seen.remove(nums[l])
                l+=1

        return False