class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        largerSum = 0
        for index in range(0,len(nums)-1,2):
            largerSum+=min(nums[index],nums[index+1])
        return largerSum
