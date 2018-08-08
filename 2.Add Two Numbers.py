# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #单个循环：如果一个list为空，补0相加
        head1=l1
        op=0
        while l1!=None and l2!=None:
            if l1.val + l2.val+op>=10:
                l1.val=(l1.val + l2.val+op)%10
                op=1
            else:
                l1.val=l1.val + l2.val+op
                op=0
            cur=l1
            l1=l1.next
            l2=l2.next
        if l2!=None:
            #print l2.val,cur.val
            cur.next=l2
            l1=cur.next
        while l1!=None:
            if l1.val+op>=10:
                l1.val=(l1.val+op)%10
                op=1
            else:
                l1.val=l1.val+op
                op=0
                
            cur=l1
            l1=l1.next
        if op==1:
            x=ListNode(1)
            cur.next=x
        return head1
