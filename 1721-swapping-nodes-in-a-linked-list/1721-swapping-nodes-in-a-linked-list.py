# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        node_arr = []

        # Traverse the linked list and store values in the array
        while head:
            node_arr.append(head.val)
            head = head.next
        
        # Swap the values
        node_arr[k-1], node_arr[-k] = node_arr[-k], node_arr[k-1]

        # Create a new linked list using the swapped values
        new_head = ListNode(node_arr[0])
        node = new_head

        for i in range(1, len(node_arr)):
            temp = ListNode(node_arr[i])
            node.next = temp
            node = node.next

        return new_head
