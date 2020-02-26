"""
        Time:
        O(nlogn) n = lenght of my list
        Space:
        O(n) n = lenght of my list
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        movements = 0
        for index, height in enumerate(sortedHeights):
            if sortedHeights[index] != heights[index]:
                movements += 1
        return movements
        
