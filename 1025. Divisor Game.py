class Solution:
    def divisorGame(self, N: int) -> bool:
        if N & 1 == 0:
            return True
        return False
