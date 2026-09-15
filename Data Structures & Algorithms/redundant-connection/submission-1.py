class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent=[i for i in range(len(edges)+1)]

        def find(node):

            while node != parent[node]:
                node=parent[node]
            return node
        
        for a,b in edges:

            A=find(a)
            B=find(b)

            if A==B:
                return [a,b]

            parent[A]=B