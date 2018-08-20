# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur  = head
        post = head
        while cur:
            flag = 0
            while cur.next and cur.next.val == cur.val: 
                flag = 1
                cur.next = cur.next.next
            if flag == 1:            
                if cur == head:
                    head = cur.next
                    cur = cur.next
                else :
                    post.next = cur.next
                    cur = cur.next                    
            else:
                post = cur
                cur = cur.next
        return head
