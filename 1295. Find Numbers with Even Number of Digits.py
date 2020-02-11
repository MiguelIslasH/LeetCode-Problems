class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenNumbers=0
        for number in nums:
            stringNumber = str(number)
            if len(stringNumber)%2==0:
                evenNumbers+=1
        return evenNumbers
