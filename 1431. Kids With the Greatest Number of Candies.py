class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greaterNumberOfCandies = -1
        isGreater = []
        
        for numberOfCandies in candies:
            print(numberOfCandies)
            if numberOfCandies > greaterNumberOfCandies:
                greaterNumberOfCandies = numberOfCandies
        
        
        for numberOfCandies in candies:
            if (numberOfCandies + extraCandies) >= greaterNumberOfCandies:
                isGreater.append(True)
            else:
                isGreater.append(False)
        
        return isGreater
