# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        # Convert nums to a set for O(1) lookups
        to_remove = set(nums)
        
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.val in to_remove:
                # Skip the node that needs to be removed
                current.next = current.next.next
            else:
                # Move to the next node if current node is not removed
                current = current.next
        
        # Return the new head of the list
        return dummy.next
