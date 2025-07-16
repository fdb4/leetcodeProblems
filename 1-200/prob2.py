# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        x=ListNode(0)
        root=x
        carov=0
        while(l1 or l2 or carov):#l1 l2 or carov must exist for the next node to exist
            val1=0
            val2=0
            if(l1): #if l1 exists assign val and move on to next node
                val1=l1.val
                l1=l1.next
            if(l2): #if l2 exists assign val and move on to next node
                val2=l2.val
                l2=l2.next
            carov,val=divmod(val1+val2+carov,10)
            x.next=ListNode(val)
            x=x.next

        return root.next
