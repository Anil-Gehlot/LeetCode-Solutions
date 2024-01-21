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


    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        length = self.size(head)

        # if there is only one node, do empty it.
        if length == 1:
            head = None
            return head

        middle = length // 2

        temp = head
        for i in range(middle-1):
            temp = temp.next
        
        if temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None

        return head



        

        
        