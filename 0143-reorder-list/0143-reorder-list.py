class ListNode:
    def __init__(self, x):
        self.val = val
        self.next = None
        
class Solution:
    def reorderList(self, head):
        slow, fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next #dividing into two halves
        slow.next = None
        
        #reversing
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        #merge two halves
        second = prev #prev is going to hold second head
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2