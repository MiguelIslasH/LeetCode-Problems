class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        operations = None
        nums = []
        for index in range(n):
            nums.append(start+(2*index))
            
        for element in nums:
            if operations == None:
                operations = element
            else:
                operations = operations ^ element
        
        return operations
        
        
"""
Simplified solution 
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        operations = None
        for index in range(n):
            if operations == None:
                operations = start+(2*index)
            else:
                operations ^= start+(2*index)
   
        return operations
"""
