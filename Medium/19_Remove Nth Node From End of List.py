# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def add_node(self,x):
            if self.next is None:
                self.next=ListNode(x)
            else:
                self.next.add_node(x)
        ListNode.add_node=add_node
        
        vals=[head.val]
        while head.next is not None:
            if head.next is not None:
                head=head.next
            vals+=[head.val]
        if len(vals)>n:
            del vals[-n]
        else:
            del vals[-len(vals)]
        if len(vals)==0:
            return None
        
        head=ListNode(vals[0])
        for val in vals[1:]:
            head.add_node(val)
        return head