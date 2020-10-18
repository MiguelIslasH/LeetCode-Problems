# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.numbers = []
    
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        self.fillNumbersList(head)
        self.numbers.reverse()
        newHead = ListNode(self.numbers[0])
        aux = newHead
        for index in range(1, len(self.numbers)):
            aux.next = ListNode(self.numbers[index])
            aux = aux.next
        aux.next = None
        
        return newHead
        
    def fillNumbersList(self, head):
        if head == None:
            return
        
        self.numbers.append(head.val)
        self.fillNumbersList(head.next)
