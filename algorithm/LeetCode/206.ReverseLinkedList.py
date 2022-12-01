class ListNode:
    def __init__(self, val=0, next=None) -> None:
        val: int = val
        next: ListNode = next


def reverseList(self, head: ListNode) -> ListNode:
    def reverse(node, prev=None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)
