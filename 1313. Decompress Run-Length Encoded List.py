"""
Time coplexity
O(n) n = Elements in nums
Space complexity
O(n) n = Elements in nums
"""
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        listDecompress = []
        for index in range(0,(len(nums)//2)):
            for _ in range(nums[2*index]):
                listDecompress.append(nums[2*index+1])
        return listDecompress
