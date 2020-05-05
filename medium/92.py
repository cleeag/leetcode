import os
from os.path import join

from src.nodes import ListNode, list_node_constructor


def reverseBetween(head: ListNode, m, n):
    if head == None or head.next == None: return head

    i = 1
    start = ListNode(0)
    start.next = head
    end = None
    p = head
    while p is not None:
        if i == m - 1 : start = p
        elif i == n:
            end = p.next
            if m == 1:
                head = p
        p = p.next
        i += 1
    print(start.next.val)

    p = start.next
    p_next = p.next
    rev_p = end
    while p.next is not end:
        p.next = rev_p
        rev_p = p
        p = p_next
        p_next = p.next
    p.next = rev_p
    start.next = p

    return head

if __name__ == '__main__':
    head = list_node_constructor([3, 5])
    print(head.val)
    reverseBetween(head, 3, 5)