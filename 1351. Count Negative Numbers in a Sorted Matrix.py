"""
Time Complexity:
O(n*m) where n = number of rows and m = number of colums
Space complexity:
O(1) Only using a few constant variables
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negativeNumbers = 0
        for row in grid:
            for index, number in enumerate(row):
                if number < 0:
                    negativeNumbers += len(row)-index
                    break
        return negativeNumbers
