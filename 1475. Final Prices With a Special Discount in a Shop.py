class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for index, number in enumerate(prices):
            minimo = self.searchMin(number, prices[index+1:])
            if minimo!=None:
                ans.append(number-minimo)
            else:
                ans.append(number)
                    
        return ans
    
    def searchMin(self, number, prices):
        for newNumber in prices:
            if newNumber<=number:
                return newNumber
        return None
    
    
