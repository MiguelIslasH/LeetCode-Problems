# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenghtOfLA = 0
        lenghtOfLB = 0
        
        pointA = headA
        pointB = headB
        while(pointA!=None):
            lenghtOfLA += 1
            pointA = pointA.next
        
        while(pointB!=None):
            lenghtOfLB += 1
            pointB = pointB.next
        
        pointA = headA
        pointB = headB
        difference = 0
        if lenghtOfLA > lenghtOfLB:
            difference = lenghtOfLA - lenghtOfLB
            for i in range(difference):
                pointA = pointA.next
        else:
            difference = lenghtOfLB - lenghtOfLA
            for i in range(difference):
                pointB = pointB.next
        while(pointA!=None and pointB!=None):
            if pointA == pointB:
                return pointA
            pointA = pointA.next
            pointB = pointB.next

        return None
        
