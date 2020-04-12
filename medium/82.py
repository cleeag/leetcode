import os
from os.path import join

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    p = head
    val_ls = []
    dup_val = set()
    while p is not None:
        if len(val_ls) > 0 and p.val == val_ls[-1]:
            dup_val.add(p.val)
        val_ls.append(p.val)
        p = p.next

    p = head
    prev = head
    i = 0
    while p is not None:
        if i == 0 and p.val in dup_val:
            head = p.next
            prev = p.next
            p = p.next
        elif i == 0:
            p = p.next
            i += 1
            if p is not None and p.val in dup_val:
                prev.next = p.next
                p = p.next
        elif p.val in dup_val:
            prev.next = p.next
            p = p.next
        else:
            p = p.next
            prev = prev.next

    return head




if __name__ == '__main__':
    pass