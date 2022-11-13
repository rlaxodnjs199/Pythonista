from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        val: int = val
        next: ListNode = next


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]):
    result_head = result = ListNode()

    while list1 and list2:
        if list1.val <= list2.val:
            result.next = list1
            list1 = list1.next
        else:
            result.next = list2
            list2 = list2.next
        result = result.next

    result = list1 or list2

    return result_head.next


"""
1. result_head = result = ListNode()를 통해 빈 ListNode를 만들고 출발점 삼음. 
   result는 계속 움직이는 포인터기 때문에 head 위치를 기억할 포인터를 하나 더 선언해야함.
2. result = l1 or l2
   if l1:
      result = l1
   if l2:
      result = l2
   대신 사용할 수 있음. or문 첫번째 값이 0 이 아니면 그 값으로 리턴.
   만약 첫번째 값이 0이고 두번째 값이 0이 아니면 두번째 값으로 리턴.
"""
