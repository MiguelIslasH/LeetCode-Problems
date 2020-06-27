class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors=[]
        i=1
        while(len(divisors)<=k and i<=n):
            if n%i==0:
                divisors.append(i)
            i+=1
            
        if len(divisors)<=k-1:
            return -1
        else:
            return divisors[k-1]
