# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None: return None
        new_head=pre=ListNode(0)
        pre.next=head
        val_=[]
        while head:
            val_.append(head.val)
            head=head.next
        val_=val_[::-1]
        for i in val_:
            pre=pre.next
            pre.val=i
        return new_head.next
        
        
        
        
