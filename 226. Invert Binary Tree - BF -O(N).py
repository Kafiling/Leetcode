# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def invertHelper(curr):
            if curr == None:
                return
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            invertHelper(curr.left)
            invertHelper(curr.right)
        invertHelper(root)
        return root
    
        
