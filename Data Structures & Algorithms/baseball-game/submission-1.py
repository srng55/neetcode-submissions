class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        summ=0

        for op in operations:

            if op=="D":
                stack.append(stack[-1]*2)
                summ+=stack[-1]
            
            elif op=="C":
                summ-=stack.pop()

            elif op=="+":
                score=stack[-1]+stack[-2]
                stack.append(score)
                summ+=score

            else:
                stack.append(int(op))
                summ+=int(op)

        return summ