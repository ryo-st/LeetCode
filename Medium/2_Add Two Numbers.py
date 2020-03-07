# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def add_node(self,x):
            if self.next is None:
                self.next=ListNode(x)
            else:
                self.next.add_node(x)
                        
        ListNode.add_node=add_node

        added_val=l1.val+l2.val
        cache=int((added_val)/10)
        l1_add_l2=ListNode((added_val)%10)       
        while l1.next is not None or l2.next is not None:
            if l1.next is not None:
                l1=l1.next
            else:
                l1=ListNode(0)
            if l2.next is not None:
                l2=l2.next
            else:
                l2=ListNode(0)
            added_val=l1.val+l2.val+cache
            cache=int((added_val)/10)
            l1_add_l2.add_node((added_val)%10)       
        if cache>0 and l1.next is None and l2.next is None:
            l1_add_l2.add_node(cache)     
        return l1_add_l2
