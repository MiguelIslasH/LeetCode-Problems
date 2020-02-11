class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        auxNumber = n
        sumOfDigits = 0
        multOfDigits = 1
        while auxNumber != 0:
            sumOfDigits += auxNumber%10
            multOfDigits *= auxNumber%10
            auxNumber//=10
        return multOfDigits - sumOfDigits
