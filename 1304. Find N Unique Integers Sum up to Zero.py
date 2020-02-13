class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 0:
            return list(0)
        elif n % 2 == 0:
            return [number for number in range(-(n//2),(n//2)+1) if number is not 0]
        else:
            return [number for number in range(-(n//2), (n//2)+1)]
