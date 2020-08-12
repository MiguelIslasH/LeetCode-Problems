class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        dp = []
        dp.append(1)
        dp.append(1)
        
        for i in range(2,10000):
            valor = dp[i-1]+dp[i-2]
            if valor> k:
                break
            dp.append(valor)
        
        cantidad = 0
        for num in reversed(dp):
            if k - num >= 0:
                k -= num
                cantidad += 1
                
            if k == 0:
                break
        return cantidad
