# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleLinkedListRecursive(self, node, carry):
        
        # If the current node is the last one
        if node.next is None:
            
            # Double the value of the current node and add carry
            double_val = (node.val * 2) + carry[0]
            
            # Update the current node's value to the last digit of the doubled value
            node.val = double_val % 10
            
            # Update carry to be used in the previous calls
            carry[0] = double_val // 10
            
            # Return the updated node and carry
            return node, carry

        # Recursively call the function for the next node
        self.doubleLinkedListRecursive(node.next, carry)
        
        #repeat the same process again if head.next is not None while moving backward by recursion
        double_val = (node.val * 2) + carry[0]
        node.val = double_val % 10
        carry[0] = double_val // 10

        # Return the updated node and carry
        return node, carry

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # Call the recursive function to double the linked list
        head, carry = self.doubleLinkedListRecursive(head, [0])

        # If there's still a carry after processing all nodes
        if carry[0] > 0:
            
            # Create a new node with the carry value and link it to the updated head
            node = ListNode(carry[0], head)
            
            # Return the new head with carry
            return node
        
        # Return the updated head
        return head
