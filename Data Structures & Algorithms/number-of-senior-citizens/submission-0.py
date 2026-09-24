class Solution:
    def countSeniors(self, details: List[str]) -> int:
        for detail in details:
            if int(detail[11:13])> 60:
                count+=1

        return count