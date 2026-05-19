# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = 1
        max_sum = root.val
        q = deque([[root]])

        curr_level = 1
        while q:
            curr_layer = q.popleft()
            layer_sum = 0
            new_layer = []
            for node in curr_layer:
                layer_sum += node.val
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)
            if layer_sum > max_sum:
                max_level = curr_level
                max_sum = layer_sum
            
            # add new layer to queue if it exists !!!
            if new_layer:
                q.append(new_layer)

            # increase level
            curr_level += 1

        return max_level
