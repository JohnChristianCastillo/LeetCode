# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find node
        if not root:
            return 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # we found the root = key
            # 3 cases
            # 1. no left child
            # 2. no right child
            # 3. 2 children -> find inorder successor

            # 1
            if not root.left:
                return root.right
            elif  not root.right:
                return root.left
            
            if root.left and root.right:
                # find inorder sucessor (left most child of right child)
                right_child = root.right
                successor = right_child
                while successor.left:
                    successor = successor.left
                # set the root to the value of the successor
                root.val = successor.val
                
                # we clean the right tree
                root.right = self.deleteNode(root.right, successor.val)
        return root