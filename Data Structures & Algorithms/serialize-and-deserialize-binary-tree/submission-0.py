# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res=[]

        def store(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))

            store(node.left)
            store(node.right)
        store(root)
        
        return ",".join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        values=data.split(",")
        i=0

        def create():
            nonlocal i
            if values[i]=="N":
                i+=1
                return None
            
            node=TreeNode(int(values[i]))
            i+=1

            node.left=create()
            node.right=create()
            return node

        return create()