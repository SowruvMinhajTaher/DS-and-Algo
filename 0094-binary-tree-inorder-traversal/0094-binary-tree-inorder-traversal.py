class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root is None:
        #     return []
        # return self.inorderTraversal(root.left)+[root.val]+ self.inorderTraversal(root.right)

        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
        