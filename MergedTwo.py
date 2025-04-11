class ListNode:
         def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list1.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
def createLinkedList(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_Linked_List(head):
    while head:
        print(head.val, end= " ->" if head.next else " ")
        head = head.next
    print()
s= Solution()
list1 = createLinkedList([1,2,4])
list2 = createLinkedList([1,3,4])
merged_list = s.mergeTwoLists(list1,list2)
print(merged_list)