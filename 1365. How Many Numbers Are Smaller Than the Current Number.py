class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = 0
        lowerNumbers = [0]*len(nums)
        for number in nums:
            for index, element in enumerate(nums):
                if index!= counter:
                    if element < number:
                        lowerNumbers[counter]+=1
            counter+=1
        return lowerNumbers
