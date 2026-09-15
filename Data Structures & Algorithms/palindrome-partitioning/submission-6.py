class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res=[]
        sol=[]

        def isPalindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1

            return True 

        def backtrack(start):
            if start == len(s):
                res.append(sol.copy())
                return

            for end in range(start,len(s)):

                #Dont pick
                if not isPalindrome(start,end):
                    continue
                #pick
                sol.append(s[start:end+1])
                backtrack(end+1)
                #undo
                sol.pop()
                    

        backtrack(0)
        return res       