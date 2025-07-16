# Merging two sorted linked lists. (yet to solve manually)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next

def createLinkedList(elements):
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

def printLinkedList(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(" -> ".join(map(str, elements)))

list1 = [int(input(f"Enter element {i+1} for the first sorted list: ")) for i in range(5)]
list2 = [int(input(f"Enter element {i+1} for the second sorted list: ")) for i in range(5)]

l1 = createLinkedList(list1)
l2 = createLinkedList(list2)

mergedList = mergeTwoLists(l1, l2)

print("Merged Linked List:")
b= (mergedList)
printLinkedList(mergedList)