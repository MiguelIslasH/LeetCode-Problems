"""
Time:
O(n) where n is the lenght of my list
Space:
O(n) where n is the lenght of my list
"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        for number in A:
            if number % 2 == 0:
                evens.append(number)
            else:
                odds.append(number)
                
        for index in range(len(A)):
            yield evens.pop() if index % 2 == 0 else odds.pop()
