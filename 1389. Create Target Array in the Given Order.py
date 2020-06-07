class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        auxIndex = 0
        for newIndex in index:
            target.insert(newIndex, nums[auxIndex])
            auxIndex += 1
        
        return target
