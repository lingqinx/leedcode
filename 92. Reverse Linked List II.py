# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i=1
        cur=head
        #遍历到m前一个并保存位置便于链接
        while cur and i<m:
            pos=cur
            cur=cur.next
            i+=1

        #中间部分思想借鉴reverse linked list
        res=None
        while cur and i<=n:
            temp=cur
            cur=cur.next
            #print cur.val
            temp.next=res
            res=temp
            i+=1
        #print res.next.next.val,res.next.val,pos.val
        if m>1:
            pos.next=res
        else:
            head=res
        while res.next:
            res=res.next
        res.next=cur
        return head
