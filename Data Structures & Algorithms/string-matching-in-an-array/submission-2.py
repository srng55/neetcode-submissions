class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        res=[]
        for word in words:
            for word2 in words:
                if word != word2 and word in word2:
                    res.append(word)
                    break
        return res
