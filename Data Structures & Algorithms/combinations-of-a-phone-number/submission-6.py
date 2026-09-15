class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res=[]
        sol=[]

        phone={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtrack(i):
            if i==len(digits):
                res.append("".join(sol))
                return

            letters=phone[digits[i]]

            for letter in letters:
                #pick
                sol.append(letter)
                backtrack(i+1)
                #undo
                sol.pop()

        if digits:
            backtrack(0)

        return res


        