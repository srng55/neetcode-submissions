class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        summ=0

        for op in operations:

            if op=="D":
                stack.append(stack[-1]*2)
            
            elif op=="C":
                summ-=stack.pop()

            elif op=="+":
                score=stack[-1]+stack[-2]
                stack.append(score)

            else:
                stack.append(int(op))

        return sum(stack)