class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected =sorted(heights)
        count=0

        for actual,exp in zip(heights,expected):
            if actual != exp:
                count+=1

        return count