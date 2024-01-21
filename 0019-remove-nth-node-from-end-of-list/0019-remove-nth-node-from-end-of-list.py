# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # finding the size of linked list.
    def size(self, head):
        temp = head
        length = 0

        if temp:
            while temp:
                temp = temp.next
                length += 1
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # if there is only one elemetn remove it
        if self.size(head) == 1:
            head = None
            return head
        
        
        # finding node no. from start to remove
        n = self.size(head) - n

        # if we are told to remove 1st node from start, then :-
        if n==0:
            head = head.next
            return head

        # getting the just previous node of the node which i have to remove.
        temp = head
        for i in range(n-1):
            temp = temp.next

        if temp.next.next :
            temp.next = temp.next.next
        else:
            temp.next = None
        
        return head


        