# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return []
        i=0
        cur=fast=slow=head
        
        while fast and i<n:#注意快指针的位置
            fast=fast.next
            i+=1
        if not fast:#若需要删掉开头一位数
            head=head.next
        else:
            while fast.next:
                fast=fast.next
                slow=slow.next
            slow.next=slow.next.next
        return head
