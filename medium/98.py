import os
from os.path import join

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root: TreeNode):
    def rec_val(node: TreeNode, larger, smaller):

        if any(node.val >= x for x in smaller) or any(node.val <= x for x in larger):
            return False

        l = r = True
        if node.left is not None:
            l = rec_val(node.left, larger, smaller + [node.val])
        if node.right is not None:
            r =  rec_val(node.right, larger + [node.val], smaller)
        if node.left is None and node.right is None:
            return True

        return r and l

    if root is None:
        return True
    else:
        ans = rec_val(root, [], [])
        return ans



if __name__ == '__main__':
    pass