class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        summ=0

        for i,op in enumerate(operations):

            if op=="D":
                stack.append(stack[-1]*2)
                summ+=stack[-1]
            
            elif op=="C":
                summ-=stack.pop()

            else:
                stack.append(int(op))
                sum+=int(op)

        return summ