class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words=s.split()
        if len( pattern) != len(words):
            return False
        
        d={}
        used=set()

        for letter,word in zip(pattern,words):
            if letter in d and d[letter]!=word:
                return False
            if letter not in d and word in used:
                return False
            
            d[letter]=word
            used.add(word)

        return True
            

