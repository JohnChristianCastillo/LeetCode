# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Deque 
    d = deque() — create an empty deque

    d.append(x) — add to the right

    d.appendleft(x) — add to the left

    d.pop() — remove from the right

    d.popleft() — remove from the left

    d[0] — peek front

    d[-1] — peek back

    len(d) — size

    d.clear()
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # idea: use a deque which stores a list 
        # --> each list represents a layer of the binary tree
        if not root:
            return []
        q = deque([[root]])
        ans = []
        while q:
            lst = q.popleft()
            rightmost = lst[-1]
            ans.append(rightmost.val)

            # gather the children of this layer's nodes
            next_layer = []
            for node in lst:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            # check first if there's even a next layer
            if next_layer:
                q.append(next_layer)

        return ans
