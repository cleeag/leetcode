import os
from os.path import join

from src.nodes import ListNode

def partition(head: ListNode, x):
    if head is None: return
    cutoff = ListNode(x - 1)
    cutoff.next = head
    prev = cutoff
    p = head

    while p :
        if p.val < x and prev != cutoff:
            tmp = p.next
            prev.next = p.next
            p.next = cutoff.next
            cutoff.next = p
            cutoff = p
            p = tmp
            if cutoff.next == head:
                head = cutoff
        elif p.val < x and prev == cutoff:
            p = p.next
            prev = prev.next
            cutoff = prev
        else:
            p = p.next
            prev = prev.next

    return head

if __name__ == '__main__':
    pass