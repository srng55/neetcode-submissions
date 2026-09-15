class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        d={}
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            d[num]=stack[-1] if stack else -1
            stack.append(num)

        return [d[num] for num in nums1]


            



        