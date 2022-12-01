class ListNode:
    def __init__(self, val=0, next=None) -> None:
        val: int = val
        next: ListNode = next


def swapPairs(self, head: ListNode) -> ListNode:
    result = prev = ListNode()

    while head and head.next:
        prev.next = head.next
        prev.next.next, head.next = head, prev.next.next
        prev = head
        head = head.next

    return result.next if result.next else head
