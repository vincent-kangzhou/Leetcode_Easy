# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        if lenA>lenB:
            for i in range(lenA-lenB):
                headA=headA.next
        elif lenA<lenB:
            for i in range(lenB-lenA):
                headB=headB.next


        while headA !=headB:
            headA=headA.next
            headB=headB.next

        return headA

    
    def getLength(self, head):
        length=0
        while head:
            length+=1
            head=head.next
        return length
        
        
        
 class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if not headA or not headB:
            return None
        
        p,q=headA, headB
        
        while p and q and p!=q:
            
            p=p.next
            q=q.next
            
            if p==q:
                return p
            
            if not p:
                p=headB
            if not q:
                q=headA
                
        return p
