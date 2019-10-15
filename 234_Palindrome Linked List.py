# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mapping=[]
        if head==None: return True
        while head:
            mapping.append(head.val)
            head=head.next
            
        left, right = 0, len(mapping)-1
        while left<right:
            if mapping[left]!=mapping[right]:
                return False
            left+=1
            right-=1
            
        return True
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mapping=[]
        if head==None or head.next==None: return True
        while head:
            mapping.append(head.val)
            head=head.next
        
        for i in range(len(mapping)//2):
            if mapping[i]!=mapping[len(mapping)-1-i]:
                return False
        return True





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:return True
        
        
        
        

        
        new_list=[]
        slow=fast=head
        
        while fast and fast.next:
            new_list.insert(0, slow.val)
            slow=slow.next
            fast=fast.next.next
            
        if fast:
            slow=slow.next
            
        for i in new_list:
            if i!=slow.val: return False
            slow=slow.next
        
        return True
        
        
        
        
        
        
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 快慢指针法找链表的中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next # slow指向链表的后半段
        slow = self.reverseList(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
