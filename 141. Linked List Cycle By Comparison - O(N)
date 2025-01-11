# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        list = [head]
        curr = head
        while curr.next != None:
            curr = curr.next
            if curr in list:
                return True
            list.append(curr)
        return False

        
