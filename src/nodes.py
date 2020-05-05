
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_node_constructor(arr:list):
    p = ListNode(arr[0])
    head = p

    for x in arr[1:]:
        p.next = ListNode(x)
        p = p.next

    return head



if __name__ == '__main__':
    pass