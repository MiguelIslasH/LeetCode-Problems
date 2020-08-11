class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for index in range(len(digits)):
            if digits[len(digits)-1-index] != 9:
                digits[len(digits)-1-index] += 1
                carry = 0
                break
            elif(digits[len(digits)-1-index] == 9):
                digits[len(digits)-1-index] = 0
                carry = 1
        if carry == 1:
            digits.insert(0,1)
        
        return digits
