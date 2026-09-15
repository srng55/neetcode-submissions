class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

    def addWord(self,word):
        node=self

        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()

            node=node.children[ch]
        node.word=word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root=TrieNode()

        for word in words:
            root.addWord(word)

        ROWS=len(board)
        COLS=len(board[0])

        res=[]
        visit=set()

        def dfs(r,c,node):
            if ( r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or 
            board[r][c] not in node.children):
                return

            visit.add((r,c))

            node=node.children[board[r][c]]

            if node.word:
                res.append(node.word)
                node.word=None

            dfs(r+1,c,node)
            dfs(r-1,c,node)
            dfs(r,c+1,node)
            dfs(r,c-1,node)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)

        return res