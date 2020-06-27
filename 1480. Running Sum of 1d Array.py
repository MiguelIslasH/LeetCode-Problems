class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumOfList = 0
        for index, number in enumerate(nums):
            nums[index] +=sumOfList
            sumOfList += number
        
        return nums
