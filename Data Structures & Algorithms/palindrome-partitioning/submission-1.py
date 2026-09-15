class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        partition=[]

        def backtrack(start):
            if start == len(s):
                res.append(partition.copy())
                return

            for end in range(start,len(s)):
                if self.isPalindrome(s,start,end):
                    partition.append(s[start:end+1])
                    backtrack(end+1)
                    partition.pop()

        backtrack(0)
        return res

    def isPalindrome(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1

        return True        