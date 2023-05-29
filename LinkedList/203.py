class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)  # initialize dummy node
        dummy.next = head  # point its next to head
        prev, curr = dummy, head  # initialize prev and curr pointers
        
        while curr:  # traverse the linked list
            if curr.val == val:  # if val found
                prev.next = curr.next  # remove the node by skipping it
            else:
                prev = curr  # move prev to the next node
            curr = curr.next  # move curr to the next node
        
        return dummy.next  # return the new head