# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack = []
        number1=""
        number2=""
        while(l1!=None):
            stack.append(l1.val) #2 4 3
            l1=l1.next
        
        for number in reversed(stack):
            number1=number1+str(number)
        stack = []
        
        while(l2!=None):
            stack.append(l2.val)
            l2=l2.next
        
        for number in reversed(stack):
            number2=number2+str(number)
        
        sumOfInversedNumbers = int(int(number1) + int(number2))
        flag=True
        pointer=ListNode(0)
        while(sumOfInversedNumbers!=0):
            digit = sumOfInversedNumbers%10
            sumOfInversedNumbers//=10
            if flag:
                solutionList = ListNode(digit)
                pointer = solutionList
                flag=False
            else:
                solutionList.next = ListNode(digit)
                solutionList = solutionList.next
        return pointer
                
                
        
