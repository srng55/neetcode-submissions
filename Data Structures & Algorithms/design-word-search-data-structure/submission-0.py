class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()


    def addWord(self, word: str) -> None:
        node=self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()

            node=node.children[ch]
        node.end=True        

    def search(self, word: str) -> bool:
        
        def dfs(j,node):
            cur=node

            for i in range(j,len(word)):
                ch=word[i]

                if ch==".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False

                if ch not in cur.children:
                    return False
                cur=cur.children[ch]

            return cur.end

        return dfs(0,self.root)    
        
