class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        hashmap={
            ')':'(',
            '}':'{',
            ']':'['

        }

        for char in s:

            if char in "([{":
                stack.append(char)

            else:
                if not stack or stack[-1] != hashmap[char]:
                    return False

                stack.pop()

        return len(stack)==0
        