class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i,ch in enumerate(strs[0]):
            for word in strs:
                if i==len(word) or word[i] != ch:
                    return ch[:i]
                
        return strs[0]
            