# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        newValue = targetSum - root.val
        print("now",root.val,"Targetsum",targetSum,newValue)
        # ทำต่อถ้า มีลูก
        if root.left is not None and self.hasPathSum(root.left, newValue):
            return True
        
        if root.right is not None and self.hasPathSum(root.right, newValue):
            return True

        if root.right is None and root.left is None:
            # ถ้ารันมาถึงตรงนี้แสดงว่า เป็น leaf node แล้ว
            # return true => target sum = 0 & is leaf
            if newValue == 0 : 
                return True
            # return false => traget sum != 0 & is leaf
            else : return False
        return False
       
        
